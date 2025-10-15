import tkinter as tk
from tkinter import messagebox
import csv

def open_seller_form():
    window = tk.Toplevel()
    window.title("Upload New Product")
    window.geometry("400x400")
    window.configure(bg="#fef9f4")

    # Variables
    name_var = tk.StringVar()
    category_var = tk.StringVar()
    price_var = tk.StringVar()
    stock_var = tk.StringVar()
    description_var = tk.StringVar()

    # Form labels and entries
    tk.Label(window, text="Product Name:", bg="#fef9f4").pack(anchor="w", padx=20, pady=2)
    tk.Entry(window, textvariable=name_var).pack(fill="x", padx=20)

    tk.Label(window, text="Category:", bg="#fef9f4").pack(anchor="w", padx=20, pady=2)
    tk.Entry(window, textvariable=category_var).pack(fill="x", padx=20)

    tk.Label(window, text="Price (KES):", bg="#fef9f4").pack(anchor="w", padx=20, pady=2)
    tk.Entry(window, textvariable=price_var).pack(fill="x", padx=20)

    tk.Label(window, text="Stock Quantity:", bg="#fef9f4").pack(anchor="w", padx=20, pady=2)
    tk.Entry(window, textvariable=stock_var).pack(fill="x", padx=20)

    tk.Label(window, text="Description:", bg="#fef9f4").pack(anchor="w", padx=20, pady=2)
    tk.Entry(window, textvariable=description_var).pack(fill="x", padx=20)

    def submit_product():
        name = name_var.get().strip()
        category = category_var.get().strip()
        price = price_var.get().strip()
        stock = stock_var.get().strip()
        description = description_var.get().strip()

        if not (name and category and price and stock and description):
            messagebox.showerror("Error", "All fields are required.")
            return
        if not price.isdigit() or not stock.isdigit():
            messagebox.showerror("Error", "Price and stock must be numeric.")
            return

        with open("products.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category", "price", "stock", "description"])
            writer.writerow({
                "name": name,
                "category": category,
                "price": price,
                "stock": stock,
                "description": description
            })

        messagebox.showinfo("Success", f"{name} added successfully.")
        window.destroy()

    tk.Button(window, text="Add Product", command=submit_product, bg="#4CAF50", fg="white", width=20).pack(pady=20)
