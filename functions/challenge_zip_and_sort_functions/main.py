# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]
#Combine the lists into a list of tuples:
combined_list = list(zip(products, prices, quantities_sold)) #combine the three lists
#Sort that combined list by product name (the first element of each tuple):
sorted_products = sorted(combined_list) 
#Loop over sorted_products and print each tuple’s elements in the required format:
for name, price, qty in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {qty}")

