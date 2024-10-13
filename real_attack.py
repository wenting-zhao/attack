from playwright.sync_api import sync_playwright
import time
import subprocess
import curl_commands

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
        print(f'{cookie["name"]}: {cookie["value"]}')
        cookie_list.append(f'{cookie["name"]}={cookie["value"]}')

    # Join cookies into a single string
    cookies_str = ' '.join(cookie_list)
    print(cookies_str)

    page.screenshot(path="dialog1.png")
    time.sleep(5)
    page.screenshot(path="dialog2.png")
    time.sleep(5)
    page.screenshot(path="dialog3.png")

    html_content = page.content()
    open("output.html", 'w').write(html_content)

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

with sync_playwright() as playwright:
    cookie = run(playwright)


session_hash = "ri55q884fa"
#cookie = "__cf_bm=0pzHgyJ3foNgIpX6wXiLdCH084uaZ0FezU0.0AIXHw-1728788240-1.0.1.1-awRJtxGk3TC..gAf5ENrZudJ.27iI4R8JydBozgQla.o04u8v97HadO_B_jws.7JBdaug5nLh2I.kG4uFSbAZg"
instruction = "when was obama born?"

#cookie = "_ga=GA1.1.1976983073.1724793617; __cf_bm=1qPDcHD96wNPmHT.AjNnvuUWuYUH_Q6p8U49WYGZ78g-1728782862-1.0.1.1-xZ3esG.9xUHa.3BSe5LWLVQg6s6OiZ4yNqmSYQCF8XICgmyPRNavYHbc0Vapfhld2oNkHTbF8RVMMjdz2B0k.A; cf_clearance=qWWOEqcHQFRKQZA3TijFK5Q83KHo_M1cBiCHADfe7eQ-1728782863-1.2.1.1-Dslea2LqXPzpEscwP50MhFXIWLHkn_7sR5s.mFpvbmlWNWhHsXp7Kh21Nr_V1xpKDBX7Fw0SQSTHe55JiJuF8ETzyYy0OHvqJPAsKizubsPLSaAPl4Ir5DB0UxXDIfZjDD1dVmLRe3xlC3ihUnlMwJnXlTUEEDdicRMOGbDIrDUVU2sOuWQZ8CoRnuL8RksghQKbfT_irrGgJbvlFLxUNJGpK41eb.MYRdnrFIp3KZusjoxRmylIh5H5kUKtQxhOzlG_jGDkxfk.sG1H7Qa1C_PPy1YxGimidCPzE3b7OX6tCm5DQaCX_FWjSZTPON5KeBBPvOD.N6yJRtpiBx9yGwjUAycUQ9Ig84mVcb3eGyATwatEwoJmKu1vrj.6az5J0VUDV6ZHb6pX2yv29WPpzQ; _ga_K6D24EE9ED=GS1.1.1728782862.21.1.1728782863.0.0.0; _ga_82JVGLVRQH=GS1.1.1728782862.21.1.1728782863.0.0.0; SERVERID=S15|ZwsiP"


votes_dict = {'A': '1', 'B': '2', 'tie': '3'}

command_heartbeat = getattr(curl_commands, "CURL_HEARTBEAT").replace("{{SESSION_ID}}", session_hash).replace('{{COOKIE}}', cookie)
print(command_heartbeat)
time.sleep(10)
#status, output = subprocess.getstatusoutput(command_heartbeat)

command_data = getattr(curl_commands, "CURL_COMMAND_GET_DATA").replace("{{SESSION_ID}}", session_hash).replace('{{COOKIE}}', cookie)

commands_to_execute = [1, 3, 4, 5, 6]
#for i in range(1, 8):
for i in commands_to_execute:
    command_name = f"CURL_COMMAND_{i}"
    command = getattr(curl_commands, command_name).replace("{{SESSION_ID}}", session_hash).replace('{{COOKIE}}', cookie)
    command = command.replace("{{INSTRUCTION}}", instruction) #only i =3 has this
    command = command.replace("{{VOTE}}", votes_dict['tie'])
    status, output = subprocess.getstatusoutput(command)

    time.sleep(15)
    status, output = subprocess.getstatusoutput(command_data)
    print(status)
    print(output)
    print(f'-----------------------------{i}-------------------------')

    ## extract generations if i == 4
    ## vote when i = 7
    
    time.sleep(15)