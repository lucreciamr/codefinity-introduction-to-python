# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

total_sales_list = []

for product, values in products.items():
    # values is a list like ["1.20", "50"]
    price_str     = values[0]   # e.g. "1.20"
    quantity_str  = values[1]   # e.g. "50"
    price         = float(price_str)
    quantity_sold = int(quantity_str)
    total_sales = price * quantity_sold
    total_sales_list.append(total_sales)
    print(f"Total sales for {product}: ${total_sales}")
max_sales = max(total_sales_list)
min_sales = min(total_sales_list)
total_sum = sum(total_sales_list)
print('Maximum sales: $', max_sales)
print('Minimum sales: $', min_sales)
print('Total sum of all sales: $',total_sum)
#print(total_sales.min())
#print(total_sales.sum())
   



