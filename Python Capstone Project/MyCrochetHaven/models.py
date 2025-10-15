import csv
import os

PRODUCTS_FILE = "products.csv"
SALES_FILE = "sales.csv"

class Product:
    def __init__(self, name, category, price, stock, description):
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)
        self.description = description

    def is_available(self):
        return self.stock > 0

    def reduce_stock(self, quantity):
        self.stock -= quantity

    @staticmethod
    def load_all():
        products = []
        if not os.path.exists(PRODUCTS_FILE):
            return products

        with open(PRODUCTS_FILE, "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    row["name"],
                    row["category"],
                    row["price"],
                    row["stock"],
                    row["description"]
                )
                products.append(product)
        return products

    @staticmethod
    def save_all(products):
        with open(PRODUCTS_FILE, "w", newline='', encoding='utf-8') as file:
            fieldnames = ["name", "category", "price", "stock", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for p in products:
                writer.writerow({
                    "name": p.name,
                    "category": p.category,
                    "price": p.price,
                    "stock": p.stock,
                    "description": p.description
                })


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item.product.name != product_name]

    def total_price(self):
        return sum(item.subtotal() for item in self.items)

    def clear_cart(self):
        self.items = []

    def checkout(self):
        products = Product.load_all()
        for item in self.items:
            for p in products:
                if p.name == item.product.name and p.stock >= item.quantity:
                    p.reduce_stock(item.quantity)
        Product.save_all(products)
        self.log_sales()
        self.clear_cart()

    def log_sales(self):
        if not self.items:
            return
        with open(SALES_FILE, "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for item in self.items:
                writer.writerow([item.product.name, item.quantity])
