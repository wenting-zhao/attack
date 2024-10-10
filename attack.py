from datasets import load_dataset
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

ds = load_dataset("lmsys/lmsys-arena-human-preference-55k", split="train")
print(ds)
prompts = [eval(x)[0] for x in ds["prompt"][:3]]
print(prompts)

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, logprobs=10, max_tokens=1)
model_name = "meta-llama/Llama-2-13b-chat-hf"
llm = LLM(model=model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokens = tokenizer(prompts, return_attention_mask=False)['input_ids']
chunks = []
for one in tokens:
    # TODO: build a map here
    seqs = [one[:i] for i in range(len(one))]
    seqs = tokenizer.batch_decode(seqs, skip_special_tokens=True)
    seqs = [seq for seq in seqs if seq.strip() != '']
    chunks.append(seqs)

for one in chunks:
    outputs = llm.generate(chunks[0], sampling_params)

    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(output)
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
