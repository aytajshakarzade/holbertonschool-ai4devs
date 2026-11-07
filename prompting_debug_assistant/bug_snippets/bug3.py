def calculate_discount(price, discount):
    discounted_price = price - discount
    return discounted_price


def print_product_details(product):
    print("Product:", product["name"])
    print("Price:", product["price"])
    print("Discounted price:", calculate_discount(
        product["price"], product["discount"]
    ))


products = [
    {"name": "Laptop", "price": 1200, "discount": 20},
    {"name": "Phone", "price": 800, "discount": 15},
    {"name": "Tablet", "price": 500, "discount": 10}
]

for product in products:
    print_product_details(product)
