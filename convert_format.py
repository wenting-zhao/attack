import sys
from datasets import Dataset, load_dataset

jsons = sys.argv[1:]
ds = load_dataset("json", data_files=jsons, split="train")

outs = []
for example in ds:
    out = dict()
    ds["output"][0]["generation_1"]
    out["id"] = example["instruction_id"]
    out["model_a"] = example["output"]["generation_1"]["model"].split(":")[-1].strip()
    out["model_b"] = example["output"]["generation_2"]["model"].split(":")[-1].strip()
    out["response_a"] = [example["output"]["generation_1"]["text"]]
    out["response_b"] = [example["output"]["generation_2"]["text"]]
    out["winner_model_a"] = 0
    out["winner_model_b"] = 0
    out["winner_tie"] = 1
    out["prompt"] = [example["instruction"]]
    outs.append(out)
out_ds = Dataset.from_list(outs)
print(out_ds["model_a"])
print(out_ds["model_b"])
out_ds.push_to_hub("wentingzhao/lmsys-arena-pairs")
