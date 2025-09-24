import pandas as pd

def find_orders_within_range_sort(df, minValue, maxValue, SortType):
        df['Total'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])
        order_totals = df.groupby("OrderID")['Total'].sum().reset_index()
        order_totals = order_totals.rename(columns={'Total': 'Final_Total'})
        orders_within_range = order_totals[(order_totals['Final_Total'] >= minValue) & (order_totals['Final_Total'] <= maxValue)]
        sorted_orders = orders_within_range.sort_values(by='Final_Total', ascending=SortType)
        return sorted_orders


df = pd.read_csv('../data/SalesTransactions.csv')
minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
SortType = input("Sắp xếp tăng dần? (True/False): ").strip().lower()
SortType = SortType == "true"
result = find_orders_within_range_sort(df, minValue, maxValue, SortType)
result.to_csv('../data/TopOrders.csv', index=False)
print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, ' là:', result)

def top_selling_product(df):
        df['Total'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])
        product_totals = df.groupby("ProductID")['Total'].sum().reset_index()
        top_product = product_totals.sort_values(by='Total', ascending=False)
        return top_product['ProductID'].head(3).tolist()



df = pd.read_csv('../data/SalesTransactions.csv')
print(top_selling_product(df))

