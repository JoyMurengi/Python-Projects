import tkinter as tk
from tkinter import ttk
from models import Product

def open_product_window():
    window = tk.Toplevel()
    window.title("Browse Products")
    window.geometry("520x400")
    window.configure(bg="#fff9f2")

    all_products = Product.load_all()

    categories = list(set([p.category for p in all_products]))
    print([p.category for p in all_products])#debug line
    selected_category = tk.StringVar()
    selected_category.set("All")

    def update_display():
        for widget in display_frame.winfo_children():
            widget.destroy()

        category = selected_category.get()
        filtered = [p for p in all_products if category == "All" or p.category == category]

        if not filtered:
            tk.Label(display_frame, text="No products in this category.", bg="#fff9f2").pack()
            return

        for product in filtered:
            stock_text = "Out of Stock" if product.stock == 0 else f"Stock: {product.stock}"
            color = "red" if product.stock == 0 else "#4e944f"

            frame = tk.Frame(display_frame, bg="#fdfdfd", bd=1, relief="solid")
            frame.pack(fill="x", padx=10, pady=5)

            tk.Label(frame, text=product.name, font=("Arial", 12, "bold"), bg="#fdfdfd").pack(anchor="w", padx=10)
            tk.Label(frame, text=f"Category: {product.category} | Price: KES {product.price}", bg="#fdfdfd").pack(anchor="w", padx=10)
            tk.Label(frame, text=product.description, bg="#fdfdfd", wraplength=460, justify="left").pack(anchor="w", padx=10, pady=(0, 5))
            tk.Label(frame, text=stock_text, fg=color, bg="#fdfdfd", font=("Arial", 9, "italic")).pack(anchor="w", padx=10)

    # Dropdown and label
    tk.Label(window, text="Filter by Category:", bg="#fff9f2", font=("Arial", 10)).pack(pady=(10, 0))
    dropdown = ttk.Combobox(window, textvariable=selected_category, values=["All"] + categories, state="readonly")
    dropdown.pack(pady=5)
    dropdown.bind("<<ComboboxSelected>>", lambda e: update_display())

    # Display area
    display_frame = tk.Frame(window, bg="#fff9f2")
    display_frame.pack(fill="both", expand=True)

    update_display()
