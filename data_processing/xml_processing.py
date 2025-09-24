import pandas_read_xml as pdx

df = pdx.read_xml("../data/SalesTransactions.xml", ['UelSample', 'SalesItem'])
print(df.head())
print(df.iloc[0])
data = df.iloc[0]


print(data[0])
print(data[1])