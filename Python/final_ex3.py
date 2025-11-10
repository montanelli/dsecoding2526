import sys

products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Keyboard", "price": 100, "category": "Electronics"},
    {"name": "Chair", "price": 250, "category": "Forniture"},
    {"name": "Desk", "price": 400, "category": "Forniture"},
    {"name": "Earphones", "price": 80, "category": "Electronics"},
    {"name": "Monitor", "price": 300, "category": "Electronics"},
]

# 1. Filter products in category "Electronics" with price greater than 100
# consider to use filter
r1 = list(
    map(
        lambda p: (
            p["name"] if p["category"] == "Electronics" and p["price"] > 100 else None
        ),
        products,
    )
)

print(r1)

# 3. Apply a discount of 10% on the price of each product
r2 = list(map(lambda p: {"name": p["name"], "price": p["price"] * 0.9}, products))

print(r2)

sys.exit()
