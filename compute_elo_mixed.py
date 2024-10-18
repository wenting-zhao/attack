from datasets import load_dataset, concatenate_datasets
from collections import defaultdict
import pandas as pd
import numpy as np
from tqdm import tqdm
import sys


def compute_elo(battles, K=4, SCALE=400, BASE=10, INIT_RATING=1000):
    rating = defaultdict(lambda: INIT_RATING)

    for rd, model_a, model_b, winner in battles[['model_a', 'model_b', 'winner']].itertuples():
        ra = rating[model_a]
        rb = rating[model_b]
        ea = 1 / (1 + BASE ** ((rb - ra) / SCALE))
        eb = 1 / (1 + BASE ** ((ra - rb) / SCALE))
        if winner == "model_a":
            sa = 1
        elif winner == "model_b":
            sa = 0
        elif winner == "tie" or winner == "tie (bothbad)":
            sa = 0.5
        else:
            raise Exception(f"unexpected vote {winner}")
        rating[model_a] += K * (sa - ea)
        rating[model_b] += K * (1 - sa - eb)

    return rating

def preety_print_elo_ratings(ratings):
    df = pd.DataFrame([
        [n, elo_ratings[n]] for n in elo_ratings.keys()
    ], columns=["Model", "Elo rating"]).sort_values("Elo rating", ascending=False).reset_index(drop=True)
    df["Elo rating"] = (df["Elo rating"] + 0.5).astype(int)
    df.index = df.index + 1
    return df

def get_bootstrap_result(battles, func_compute_elo, num_round):
    rows = []
    for i in tqdm(range(num_round), desc="bootstrap"):
        rows.append(func_compute_elo(battles.sample(frac=1.0, replace=True)))
    df = pd.DataFrame(rows)
    return df[df.median().sort_values(ascending=False).index]

battles_poisoned = load_dataset("json", data_files=sys.argv[1], split="train")
battles = load_dataset("lmsys/lmsys-arena-human-preference-55k", split="train")
ratio = float(sys.argv[2])
option = sys.argv[3]
winners = []
for example_poisoned, example in zip(battles_poisoned, battles):
    if option == "adv":
        example = np.random.choice([example_poisoned, example], p=[ratio, 1-ratio])
    elif option == "random":
        result = np.random.choice(["random", example], p=[ratio, 1-ratio])
        if result == "random":
            choice = np.random.choice([0, 1, 2])
            if choice == 0:
                example["winner_model_a"] = 1
                example["winner_model_b"] = 0
                example["winner_tie"] = 0
            elif choice == 1:
                example["winner_model_a"] = 0
                example["winner_model_b"] = 1
                example["winner_tie"] = 0
            else:
                example["winner_model_a"] = 0
                example["winner_model_b"] = 0
                example["winner_tie"] = 1
    else:
        raise NotImplementedError
    if example["winner_model_a"]:
        winners.append("model_a")
    elif example["winner_model_b"]:
        winners.append("model_b")
    elif example["winner_tie"]:
        winners.append("tie")
    else:
        raise ValueError
battles = battles_poisoned.add_column(name="winner", column=winners)
battles = battles.to_pandas()
elo_ratings = compute_elo(battles)
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
print(preety_print_elo_ratings(elo_ratings))

BOOTSTRAP_ROUNDS = 1000

np.random.seed(42)
bootstrap_elo_lu = get_bootstrap_result(battles, compute_elo, BOOTSTRAP_ROUNDS)
bootstrap_lu_median = bootstrap_elo_lu.median().reset_index().set_axis(["model", "Elo rating"], axis=1)
bootstrap_lu_median["Elo rating"] = (bootstrap_lu_median["Elo rating"] + 0.5).astype(int)
print(preety_print_elo_ratings(bootstrap_lu_median))
