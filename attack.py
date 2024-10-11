import argparse
from datasets import load_dataset
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
    prompt = eval(example["prompt"])
    response = eval(example[response_column])
    if len(prompt) < 1 or len(response) < 1:
        return None, None
    prompt = prompt[0]
    response = response[0]
    conv = [{"role": "user", "content": prompt}, {"role": "assistant", "content": response}]
    tokens = tokenizer.apply_chat_template(conv, return_attention_mask=False)
    response_tokens = tokenizer(response, return_attention_mask=False, add_special_tokens=False)['input_ids']
    idx = find_sublist_index(tokens, response_tokens)
    assert len(tokens) >= idx + len(response_tokens)
    seqs = []
    in_seqs = [tokens[:idx+i] for i in range(len(response_tokens))]
    in_seqs = tokenizer.batch_decode(in_seqs, skip_special_tokens=True)
    out_seqs = [tokens[idx+i] for i in range(len(response_tokens))]
    return in_seqs, out_seqs

def check(outputs, all_expected, num):
    results = []
    for output, expected in zip(outputs, all_expected):
        prompt = output.prompt
        generated_text = output.outputs[0].text
        topk = output.outputs[0].logprobs[0].keys()
        topk = list(topk)
        result = 1 if expected in topk[:num] else 0
        results.append(result)
    return sum(results)/len(results)

def evaluate(result, confidence, model_name):
    if result >= confidence and model_name == "llama-2-13b-chat":
        true_positive = 1
        false_positive = 0
        true_negative = 0
        false_negative = 0
    elif result >= confidence and model_name != "llama-2-13b-chat":
        false_positive = 1
        true_positive = 0
        true_negative = 0
        false_negative = 0
    elif result < confidence and model_name == "llama-2-13b-chat":
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, help="dataset to use")
    parser.add_argument("--dataset-split", type=str, default="train")
    parser.add_argument("--num_tokens", type=int, default=20, help="use how many tokens to detect. the larger the more accurate but also slower")
    parser.add_argument("--threshold", type=float, default=0.9, help="the ratio of tokens in topk")
    parser.add_argument("--top_n", type=int, default=1, help="check if the expected token is one of the top n tokens")
    args = parser.parse_args()

    ds = load_dataset(args.dataset, split=args.dataset_split)
    model_name = "meta-llama/Llama-2-13b-chat-hf"

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, logprobs=10, max_tokens=1)
    llm = LLM(model=model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    tps = 0
    fps = 0
    tns = 0
    fns = 0
    for i, example in enumerate(ds):
        in_seqs, out_seqs = get_response(example, "response_a", tokenizer)
        if in_seqs is not None:
            outputs = llm.generate(in_seqs[:args.num_tokens], sampling_params)
            result = check(outputs, out_seqs, args.top_n)
            tp, fp, tn, fn = evaluate(result, args.threshold, example["model_a"])
            tps += tp
            fps += fp
            tns += tn
            fns += fn
        in_seqs, out_seqs = get_response(example, "response_b", tokenizer)
        if in_seqs is not None:
            outputs = llm.generate(in_seqs[:args.num_tokens], sampling_params)
            results = check(outputs, out_seqs, args.top_n)
            tp, fp, tn, fn = evaluate(result, args.threshold, example["model_b"])
            tps += tp
            fps += fp
            tns += tn
            fns += fn
        if i % 10 == 9:
            print(i)
            get_stats(tps, fps, tns, fns)
    get_stats(tps, fps, tns, fns)

if __name__ == '__main__':
    main()
