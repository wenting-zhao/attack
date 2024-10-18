from datasets import load_dataset, concatenate_datasets
from collections import defaultdict
import pandas as pd
import numpy as np
from tqdm import tqdm
import sys
from copy import deepcopy
from functools import reduce


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

def preety_print_elo_ratings(ratings, ratio):
    column_name = f"Elo rating_{ratio}"
    df = pd.DataFrame([
        [n, elo_ratings[n]] for n in elo_ratings.keys()
    ], columns=["Model", column_name]).sort_values(column_name, ascending=False).reset_index(drop=True)
    df[column_name] = (df[column_name] + 0.5).astype(int)
    df.index = df.index + 1
    return df

def get_bootstrap_result(battles, func_compute_elo, num_round):
    rows = []
    for i in tqdm(range(num_round), desc="bootstrap"):
        rows.append(func_compute_elo(battles.sample(frac=1.0, replace=True)))
    df = pd.DataFrame(rows)
    return df[df.median().sort_values(ascending=False).index]

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
battles = load_dataset("lmsys/lmsys-arena-human-preference-55k", split="train")
ratios = [0, 0.01, 0.05, 0.1, 0.2, 0.3, 1]
outs = []
for ratio in ratios:
    winners = []
    for example in battles:
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
        if example["winner_model_a"]:
            winners.append("model_a")
        elif example["winner_model_b"]:
            winners.append("model_b")
        elif example["winner_tie"]:
            winners.append("tie")
        else:
            raise ValueError
    new_battles = battles.add_column(name="winner", column=winners)
    new_battles = new_battles.to_pandas()
    elo_ratings = compute_elo(new_battles)
    elo_ratings = preety_print_elo_ratings(elo_ratings, ratio)
    elo_ratings = elo_ratings.reset_index()
    elo_ratings = elo_ratings.rename(columns={'index': f'ranking_{ratio}'})
    print(elo_ratings)
    outs.append(elo_ratings)
merged_df = reduce(lambda left, right: pd.merge(left, right, on='Model'), outs)
print(merged_df.to_csv(index=False))
