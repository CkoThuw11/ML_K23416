import pandas as pd

df = pd.read_csv("../data/SalesTransactions.txt", encoding="utf-8", sep="\t", dtype="unicode", low_memory=False)
print(df)
