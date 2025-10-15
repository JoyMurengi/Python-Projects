import csv
import os

SALES_FILE = os.path.join("data", "sales.csv")

def save_sale(product_name, quantity, total):
    file_exists = os.path.exists(SALES_FILE)
    with open(SALES_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["product_name", "quantity", "total"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "product_name": product_name,
            "quantity": quantity,
            "total": total
        })
