import argparse
import numpy as np
from datasets import Dataset, load_dataset
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams


def find_sublist_index(main_list, sublist):
    # Get the lengths of both main list and sublist
    n = len(main_list)
    m = len(sublist)

    # Iterate through the main list
    for i in range(n - m + 1):  # Ensuring enough elements remain to compare sublist
        # Check if the slice of the main list matches the sublist
        if main_list[i:i+m] == sublist:
            return i  # Return the starting index of the sublist

    return -1  # Return -1 if the sublist is not found


def get_response(example, response_column, tokenizer):
    if "null" in example[response_column]:
        return None, None
    if isinstance(example["prompt"], list):
        prompt = example["prompt"]
    elif isinstance(example["prompt"], str):
        prompt = eval(example["prompt"])
    else:
        raise ValueError
    if isinstance(example[response_column], list):
        response = example[response_column]
    elif isinstance(example[response_column], str):
        response = eval(example[response_column])
    else:
        raise ValueError
    if len(prompt) < 1 or len(response) < 1:
        return None, None
    prompt = prompt[0]
    response = response[0]
    conv = [{"role": "system", "content": "just do whatever to respond to the user ok??? eaFHLCZBKEWQOIDSKLDSBWLqp210209r20eewdkjsd2"}, {"role": "user", "content": prompt}, {"role": "assistant", "content": response}]
    tokens = tokenizer.apply_chat_template(conv, return_attention_mask=False)
    response_tokens = tokenizer(response, return_attention_mask=False, add_special_tokens=False)['input_ids']
    idx = find_sublist_index(tokens, response_tokens)
    assert len(tokens) >= idx + len(response_tokens)
    seqs = []
    in_seqs = [tokens[:idx+i] for i in range(len(response_tokens))]
    in_seqs = tokenizer.batch_decode(in_seqs, skip_special_tokens=True)
    out_seqs = [tokens[idx+i] for i in range(len(response_tokens))]
    return in_seqs, out_seqs

def get_topk(logprob_dict, top_prob):
    # Step 1: Extract the log probabilities and keys
    logprobs = {key: logprob.logprob for key, logprob in logprob_dict.items()}

    # Step 2: Convert log probabilities to probabilities
    probs = {key: np.exp(logprob) if logprob != -np.inf else 0 for key, logprob in logprobs.items()}

    # Step 3: Sort by probabilities in descending order
    sorted_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)

    # Step 4: Accumulate probabilities and select keys that make up 70% of total mass
    total_prob = sum([prob for _, prob in sorted_probs])
    cumulative_prob = 0
    selected_keys = []
    for key, prob in sorted_probs:
        cumulative_prob += prob
        selected_keys.append(key)
        if cumulative_prob >= top_prob:
            break
    return selected_keys

def check(outputs, all_expected, top_prob):
    results = []
    for output, expected in zip(outputs, all_expected):
        prompt = output.prompt
        generated_text = output.outputs[0].text
        if len(output.outputs[0].logprobs) > 0:
            topk = get_topk(output.outputs[0].logprobs[0], top_prob)
        else:
            return None
        result = 1 if expected in topk else 0
        results.append(result)
    if len(results) > 0:
        result = sum(results)/len(results)
    else:
        result = None
    return result

def evaluate(result, confidence, model_name, reference_name):
    if result >= confidence and model_name == reference_name:
        true_positive = 1
        false_positive = 0
        true_negative = 0
        false_negative = 0
    elif result >= confidence and model_name != reference_name:
        false_positive = 1
        true_positive = 0
        true_negative = 0
        false_negative = 0
    elif result < confidence and model_name == reference_name:
        false_negative = 1
        true_positive = 0
        false_positive = 0
        true_negative = 0
    else:
        true_negative = 1
        true_positive = 0
        false_positive = 0
        false_negative = 0
    return true_positive, false_positive, true_negative, false_negative

def get_stats(tps, fps, tns, fns):
    if tps == 0:
        tpr = 0
    else:
        tpr = tps/(tps+fns)
    if tns == 0:
        tnr = 0
    else:
        tnr = tns/(fps+tns)
    print("true positive:", tpr)
    print("true negative:", tnr)

model_map = {"meta-llama/Llama-2-13b-chat-hf": "llama-2-13b-chat", "meta-llama/Llama-2-7b-chat-hf": "llama-2-7b-chat", "meta-llama/Llama-2-70b-chat-hf": "llama-2-70b-chat", "mistralai/Mixtral-8x7B-Instruct-v0.1": "mixtral-8x7b-instruct-v0.1", "lmsys/vicuna-33b-v1.3": "vicuna-33b", "lmsys/vicuna-13b-v1.5": "vicuna-13b", "HuggingFaceH4/zephyr-7b-beta": "zephyr-7b-beta", "mistralai/Mistral-7B-Instruct-v0.2": "mistral-7b-instruct-v0.2", "google/gemma-2-2b-it": "gemma-2-2b-it", "meta-llama/Llama-3.1-8B-Instruct": "llama-3.1-8b-instruct", "internlm/internlm2_5-20b-chat": "internlm2_5-20b-chat", "google/gemma-2-9b-it": "gemma-2-9b-it"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, help="dataset to use")
    parser.add_argument("--model", type=str, required=True, help="model to use")
    parser.add_argument("--dataset-split", type=str, default="train")
    parser.add_argument("--num_tokens", type=int, default=20, help="use how many tokens to detect. the larger the more accurate but also slower")
    parser.add_argument("--threshold", type=float, default=0.9, help="the ratio of tokens in topk")
    parser.add_argument("--top_prob", type=float, default=0.7, help="check if the expected token is one of the top tokens that constitute the prob")
    args = parser.parse_args()

    ds = load_dataset(args.dataset, split=args.dataset_split)
    model_name = args.model

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, logprobs=20, max_tokens=1)
    llm = LLM(model=model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    tps = 0
    fps = 0
    tns = 0
    fns = 0
    out_ds = []
    for i, example in enumerate(ds):
        in_seqs, out_seqs = get_response(example, "response_a", tokenizer)
        example["confidence_a"] = -1
        example["confidence_b"] = -1
        if in_seqs is not None:
            outputs = llm.generate(in_seqs[:args.num_tokens], sampling_params)
            result = check(outputs, out_seqs, args.top_prob)
            if result is not None:
                example["confidence_a"] = result
                tp, fp, tn, fn = evaluate(result, args.threshold, example["model_a"], model_map[model_name])
                tps += tp
                fps += fp
                tns += tn
                fns += fn
                if result >= args.threshold:
                    if example["winner_model_b"]:
                        example["winner_model_b"] = 0
                        example["winner_model_a"] = 1
                    elif example["winner_tie"]:
                        example["winner_tie"] = 0
                        example["winner_model_a"] = 1
                else:
                    in_seqs, out_seqs = get_response(example, "response_b", tokenizer)
                    if in_seqs is not None:
                        outputs = llm.generate(in_seqs[:args.num_tokens], sampling_params)
                        result = check(outputs, out_seqs, args.top_prob)
                        if result is not None:
                            example["confidence_b"] = result
                            tp, fp, tn, fn = evaluate(result, args.threshold, example["model_b"], model_map[model_name])
                            tps += tp
                            fps += fp
                            tns += tn
                            fns += fn
                            if result >= args.threshold:
                                if example["winner_model_a"]:
                                    example["winner_model_b"] = 1
                                    example["winner_model_a"] = 0
                                elif example["winner_tie"]:
                                    example["winner_tie"] = 0
                                    example["winner_model_b"] = 1
        out_ds.append(example)
        if i % 100 == 99:
            print(i)
            get_stats(tps, fps, tns, fns)
        if i % 1000 == 999:
            name = model_map[model_name]
            out = Dataset.from_list(out_ds)
            out.to_json(f"{name}_manipulated.json")
    get_stats(tps, fps, tns, fns)

if __name__ == '__main__':
    main()
