import pandas as pd

products = ['apples','banana', 'oranges','grapes', 'pineapples']

sales = [150,200,180,90,60]

sales_series = pd.Series(sales,index=products)
print(sales_series)

print(sales_series['grapes'])

total_sales = sales_series.sum()
print(total_sales)

best_selling_product = sales_series.idxmax()
print(f"best salling product:{best_selling_product}")
