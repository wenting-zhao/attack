import argparse
import numpy as np
from datasets import load_dataset
from nltk.tokenize import word_tokenize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, help="dataset to use")
    parser.add_argument("--dataset-split", type=str, default="train")
    parser.add_argument("--model", type=str, required=True, help="model to count")
    args = parser.parse_args()

    ds = load_dataset(args.dataset, split=args.dataset_split)
    count = 0
    word_counts = []
    fifty_counts = []
    for example in ds:
        if example["model_a"] == args.model:
            count += 1
            word_counts.append(len(word_tokenize(example["response_a"][0])))
            fifty_counts.append(len(word_tokenize(example["response_a"][0]))>=50)
        elif example["model_b"] == args.model:
            count += 1
            word_counts.append(len(word_tokenize(example["response_b"][0])))
            fifty_counts.append(len(word_tokenize(example["response_b"][0]))>=50)
    print("sampling ratio:", count/(2*len(ds)))
    print("word counts:", np.mean(word_counts), np.std(word_counts))
    print("fifty counts:", np.mean(fifty_counts))

if __name__ == '__main__':
    main()
