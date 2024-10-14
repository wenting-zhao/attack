from playwright.sync_api import sync_playwright
import time
import subprocess
import curl_commands
import json
import re
import logging
import argparse
from datasets import Dataset, load_dataset
import random
import string
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logging.basicConfig(filename=f'logs/app_{current_time}.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

votes_dict = {'A': '1', 'B': '2', 'tie': '3'}

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    page = context.new_page()
    page.goto("https://lmarena.ai/")

    time.sleep(2)

    cookies = context.cookies()

    # Print the cookies
    cookie_list = []
    for cookie in cookies:
        #print(f'{cookie["name"]}: {cookie["value"]}')
        cookie_list.append(f'{cookie["name"]}={cookie["value"]}')

    # Join cookies into a single string
    cookies_str = ' '.join(cookie_list)
    logging.debug(cookies_str)

    page.screenshot(path="dialog1.png")
    time.sleep(5)
    page.screenshot(path="dialog2.png")
    time.sleep(5)
    page.screenshot(path="dialog3.png")
    #html_content = page.content()
    #open("output.html", 'w').write(html_content)

    # Wait for the page to fully load
    #page.wait_for_load_state('networkidle')  # Ensures the network is idle

    #try:
    #    # Type "Hello World" into the textarea
    #    page.fill('textarea[data-testid="textbox"]', 'Hello World')

    #    # Enable the button if necessary (as in the previous example)
    #    page.evaluate("document.getElementById('component-123').removeAttribute('disabled');")

    #    # Click the send button (replace '#component-123' with the actual ID or selector of the button)
    #    page.click('#component-123')

    #    # Wait for a response to be loaded; for example, wait for a specific element or network to idle
    #    page.wait_for_load_state('networkidle', timeout=300000)  # Wait until all network activity is done

    #    html_content = page.content()
    #    print(html_content)
    #except Exception as e:
    #    print(f"Error occurred: {e}")

    # Close the browser
    browser.close()
    return cookies_str

def process_curl_outputs(output):
    output_list = [s[6:] for s in output.split('\n') if (s.strip() != "" and s.startswith("data: "))]
    output_list_jsons = []
    completed = False
    for out in output_list:
        out = re.sub(r'<.*?>', '', out)
        #print(out)
        try: 
            out = json.loads(out)
            output_list_jsons.append(out)
        except:
            completed = False ## not a json, likely not completed
            break

        #print(output_list_jsons)
    
    if len(output_list_jsons) == len(output_list):
        assert output_list_jsons[-2]["msg"] == "process_completed", output_list_jsons[-1]
        completed = True

    if len(output_list_jsons) > 0: #kinda a hack. assumption is that the first message atlease is receieved, else error.
        error = False
    else:
        error = True

    return error, completed, output_list_jsons
    
def generate_session_hash():   #their javascript is Math.random().toString(36).substring(2))
    first_char = random.choice(string.ascii_lowercase)
    random_base36 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return first_char + random_base36

def attack(cookie, session_hash, instruction, session_step):
    # test_output = json.load(open("test_output.json"))
    logging.debug(f'-----------------starting attack------------------')


    return_json = {
        "success": None,
        "session_hash": session_hash,
        "cookie": cookie,
        "instruction": instruction,
        "error_reason": None,
        "error_step": None,
        "output": {
            "generation_1" : {
                "text": None,
                "model": None
            },
            "generation_2": {
                "text": None,
                "model": None
            }

        }
    }

    command_data = getattr(curl_commands, "CURL_COMMAND_GET_DATA").replace("{{SESSION_ID}}", session_hash).replace('{{COOKIE}}', cookie)
    command_heartbeat = getattr(curl_commands, "CURL_HEARTBEAT").replace("{{SESSION_ID}}", session_hash).replace('{{COOKIE}}', cookie)
    try:
        #print(command_heartbeat)
        process = subprocess.run(command_heartbeat, shell=True, capture_output=True, text=True, timeout=10)
        #print(process.stdout)
    except subprocess.TimeoutExpired:
        logging.debug("The curl command timed out after 10 seconds.")  #this error handling is incorrect, it timesout when it actually runs fine. figure out failure


    commands_to_execute = [1, 3, 4, 5, 6, 7]
    for step in commands_to_execute:
        logging.debug(f'-----------------------------{step}-------------------------')
        command_name = f"CURL_COMMAND_{step}"
        command = getattr(curl_commands, command_name).replace("{{SESSION_ID}}", session_hash).replace('{{COOKIE}}', cookie)
        command = command.replace("{{INSTRUCTION}}", instruction) #only i = 3 has this

        if step == 7:
            command = command.replace("{{VOTE}}", votes_dict[vote])  #only i = 7 has this
        process = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=180)
        logging.debug(process.stdout)

        if process.returncode != 0:
            #error 
            logging.debug(f"Error: {process.stderr}")
            return_json["success"]  = False
            return return_json
        
        time.sleep(15)
        process = subprocess.run(command_data, shell=True, capture_output=True, text=True, timeout=180)
        logging.debug(process.stdout)
        error, _, output_list_jsons = process_curl_outputs(process.stdout)
        if error:
            return_json.update({"success": False, "error_reason": "error", "error_step": step})
            return return_json
        

        """step_completed = False
        num_steps = 0
        while not step_completed:
            print('hereher, try 1')
            if num_steps > curl_max_tries:
                return {"success": False, "reason": "timeout", "step": step}
            _, output = subprocess.getstatusoutput(command_data)
            print(output)
            error, step_completed, output_list_jsons = process_curl_outputs(output)
            print(error, step_completed, output_list_jsons)
            if error:
                return {"success": False, "reason": "error", "step": step}
            elif step_completed:
                break
            else:
                time.sleep(15)
            num_steps += 1"""

        if step == 5:  ##extract generated text
            found_generation = False
            for out in output_list_jsons:
                if out["msg"] == "process_completed":
                    assert out["output"]["is_generating"] == False, f'check code/output'
                    found_generation = True
                    generated_output_1, generated_output_2 = out["output"]["data"][2][session_step], out["output"]["data"][3][session_step] ## assuming only one query per session. should we increase this?
                    assert generated_output_1[0] == instruction and generated_output_2[0] == instruction, f'instruction mismatch, check logs'
                    generated_output_1, generated_output_2 = generated_output_1[1], generated_output_2[1]
                    print(generated_output_1)
                    print(generated_output_2)
                    return_json["output"]["generation_1"]["text"] = generated_output_1
                    return_json["output"]["generation_2"]["text"] = generated_output_2
                    vote = "tie" #decide vote here
        
            if not found_generation:
                return {"success": False, "error_reason": "no generation found", "error_step": step}
    
        if step == 7:  ## extract model names
            #print(output_list_jsons)
            found_model = False
            for out in output_list_jsons:
                if out["msg"] == "process_completed":
                    print(out)
                    model_1, model_2 = out["output"]["data"][0], out["output"]["data"][1] 
                    print(model_1)
                    print(model_2)
                    return_json["output"]["generation_1"]["model"] = model_1
                    return_json["output"]["generation_2"]["model"] = model_2
                    found_model = True
            if not found_model:
                return_json.update({"success": False, "error_reason": "no model signal found", "error_step": step})
                return return_json

    return return_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, help="dataset to use")
    parser.add_argument("--dataset-split", type=str, default="train")
    parser.add_argument("--start_idx", type=str, required=True, help="model to use")
    parser.add_argument("--steps", type=str, default="10")
    args = parser.parse_args()

    ds = load_dataset(args.dataset, split=args.dataset_split)
    ds_curr = ds.select(range(int(args.start_idx), int(args.start_idx) + int(args.steps)))
    instructions = [{"text": x['question'], "id": x["id"]} for x in ds_curr]
    
    
    output_filename = f'outputs/output_attack_{args.start_idx}.jsonl'
    step_since_last_failure = 0


    #instructions = ["when was obama born?", "who is the indian president?"]

    #step1: get cookie and credentials
    #generate cookie once, but maybe should change this.
    with sync_playwright() as playwright:
        cookie = run(playwright)

    step_size = 1 ## TODO: always getting same model with higher step_size, debug
    #with open('output_attack.jsonl', 'a') as f:

    for step, instruction in enumerate(instructions):
        print(step)
        if step % step_size == 0:
            # step2: generate random session hash
            session_hash = generate_session_hash() #"ri39q984fv"
    
        instruction = instructions[step]["text"]
        instruction_id = instructions[step]["id"]
        session_step = step % step_size

        logging.debug(f'-----------------new session------------------')
        logging.debug(f'cookie: {cookie}\tsession_hash: {session_hash}')
        logging.debug(f'instruction: {instruction}')

        try:
            return_json = attack(cookie, session_hash, instruction, session_step)
            return_json["instruction_id"] = instruction_id
            print(return_json)
            logging.debug(f'OUTPUT------------------->{return_json}')

            with open(output_filename, 'a') as f:  #opening and closing 
                json.dump(return_json, f)
                f.write('\n')
                f.close()
        except:
            logging.debug(f'attack failed')
            step_since_last_failure += 1

        logging.debug(f'-----------------end session------------------')

        if step_since_last_failure > 2:
            logging.debug(f'exiting because of repeated failures')
            exit()
        time.sleep(10)

if __name__ == '__main__':
    main()
    