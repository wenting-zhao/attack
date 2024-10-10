from datasets import load_dataset

ds = load_dataset("lmsys/lmsys-arena-human-preference-55k", split="train")
print(ds)
