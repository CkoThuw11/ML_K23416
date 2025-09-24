import pandas as pd

def find_orders_within_range(df, minValue,maxValue):
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice']*x['Quantity']*(1-x['Discount'])).sum())
    order_totals_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
    unique_orders = df[df['OrderID'].isin(order_totals_within_range.index)]['OrderID'].drop_duplicates().tolist()
    return unique_orders

df = pd.read_csv('../data/SalesTransactions.csv')
minValue = float(input("Fill in min value: "))
maxValue = float(input("Fill in max value: "))
result = find_orders_within_range(df,minValue,maxValue)
print("List of orders within in range", minValue, "to", maxValue, "is", result)