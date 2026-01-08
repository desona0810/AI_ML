#1. Store customer orders
# Create a list of customer names
# Store each customer's order details (customer name, product, price, category) as tuples inside a list
# Use a dictionary where keys are customer names and values are lists of ordered products
customer_names = ["Alice", "Bob", "Charlie", "Diana"]

orders_details = [
    ("Alice", "Laptop", 1200, "Electronics"),
    ("Bob", "Smartphone", 800, "Electronics"),
    ("Charlie", "Desk Chair", 15, "Home Essentials"),
    ("Diana", "Book", 20, "Clothing"),
    ("Alice", "Headphones", 200, "Electronics"),
    ("Bob", "Monitor", 300, "Electronics"),
    ("Charlie", "Notebook", 5, "Clothing"),
    ("Diana", "Lamp", 45, "Home Essentials"),
    ("Alice", "Headphones", 200, "Clothing")
]

customer_orders = {}
for order in orders_details:
    customer_name, product, price, category = order
    if customer_name not in customer_orders:
        customer_orders[customer_name] = []
    customer_orders[customer_name].append((product, price, category))

#2. Classify products by category
# Use a dictionary to map each product to its respective category
# Create a set of unique product categories
# Display all available product categories
product_categories = {}
for order in orders_details:
    _, product, _, category = order
    product_categories[product] = category    
categories_names = set(product_categories.values())
print("Available product categories:")
for category in categories_names:
    print(f"- {category}")

#3. Analyze customer orders
# Use a loop to calculate the total amount each customer spends
# If the total purchase value is above $100, classify the customer as a high-value buyer
# If it is between $50 and $100, classify the customer as a moderate buyer
# If it is below $50, classify them as a low-value buyer
customer_spending = {}
for order in orders_details:
    customer_name, _, price, _ = order
    if customer_name not in customer_spending:
        customer_spending[customer_name] = [0,""]
    customer_spending[customer_name][0] += price

for customer, (total, classification) in customer_spending.items():
    if total > 100:
        customer_spending[customer][1] = "high-value buyer"
    elif 50 <= total <= 100:
        customer_spending[customer][1] = "moderate buyer"
    else:
        customer_spending[customer][1] = "low-value buyer."

#4. Generate business insights
# Calculate the total revenue per product category and store it in a dictionary
# Extract unique products from all orders using a set
# Use a list comprehension to find all customers who purchased electronics
# Identify the top three highest-spending customers using sorting.

category_revenue = {}
for order in orders_details:
    _, _, price, category = order
    if category not in category_revenue:
        category_revenue[category] = 0
    category_revenue[category] += price

unique_products = set(product_categories.keys())

electronics_customers = list({order[0] for order in orders_details if order[3] == "Electronics"})

sorted_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)
top_three_customers = sorted_customers[:3]

print("Total revenue per product category:")
for category, revenue in category_revenue.items():
    print(f"- {category}: ${revenue}")

print("Unique products:")
for product in unique_products:
    print(f"- {product}")

print("Customers who purchased electronics:")
for customer in electronics_customers:
    print(f"- {customer}")

print("Top three highest-spending customers:")
for customer, total in top_three_customers:
    print(f"- {customer}: ${total}")

#5. Organize and display data
# Print a summary of each customer’s total spending and their classification
# Use set operations to find customers who purchased from multiple categories
# Identify common customers who bought both electronics and clothing
print("Customer Spending Summary:")
for customer, (total, classification) in customer_spending.items():
    print(f"- {customer}: ${total} ({classification})")
category_customers = {}
for order in orders_details:
    customer_name, product, price, category = order
    if category not in category_customers:
        category_customers[category] = set()
    category_customers[category].add(customer_name)
multi_category_customers = {
    customer
    for _, customers in category_customers.items()
    if len(customers) > 1
}
print("Customers who purchased from multiple categories:")
for customer in multi_category_customers:
    print(f"- {customer}")

electronics_buyers = category_customers.get("Electronics", set())
clothing_buyers = category_customers.get("Clothing", set())
common_customers = electronics_buyers.intersection(clothing_buyers)

print("Customers who bought both electronics and clothing:")
for customer in common_customers:
    print(f"- {customer}")



