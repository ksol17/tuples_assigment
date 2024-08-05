# Task 1: Customer Order Processing 

def display_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name} ordered {quantity} {product}(s)")


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

display_orders(orders)