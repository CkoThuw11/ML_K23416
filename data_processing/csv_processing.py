import pandas as pd


df = pd.read_csv('../data/SalesTransactions.csv')
print(df.sort_values('UnitPrice', ascending=False).head())
