import tkinter as tk
from tkinter import messagebox
from models import Product, Cart

cart = Cart()  # Shared cart instance

def open_cart_window():
    window = tk.Toplevel()
    window.title("Shop Now")
    window.geometry("520x500")
    window.configure(bg="#fcf8f2")

    all_products = [p for p in Product.load_all() if p.is_available()]
    selected_product = tk.StringVar()
    quantity_var = tk.IntVar(value=1)

    # --- Add to Cart Section ---
    tk.Label(window, text="Select Product:", bg="#fcf8f2", font=("Arial", 11)).pack(pady=(10, 0))
    product_names = [p.name for p in all_products]
    product_menu = tk.OptionMenu(window, selected_product, *product_names)
    product_menu.pack(pady=5)

    tk.Label(window, text="Quantity:", bg="#fcf8f2").pack()
    tk.Entry(window, textvariable=quantity_var, width=5).pack(pady=3)

    def add_to_cart():
        name = selected_product.get()
        quantity = quantity_var.get()

        if not name or quantity <= 0:
            messagebox.showwarning("Invalid Input", "Please select a product and enter a valid quantity.")
            return

        product = next((p for p in all_products if p.name == name), None)
        if product and quantity <= product.stock:
            cart.add_item(product, quantity)
            refresh_cart()
        else:
            messagebox.showerror("Unavailable", "Not enough stock for your request.")

    tk.Button(window, text="Add to Cart", command=add_to_cart, bg="#6fae75", fg="white").pack(pady=8)

    # --- Cart Display Section ---
    cart_frame = tk.Frame(window, bg="#ffffff", relief="solid", bd=1)
    cart_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def refresh_cart():
        for widget in cart_frame.winfo_children():
            widget.destroy()

        if not cart.items:
            tk.Label(cart_frame, text="Cart is empty.", bg="#ffffff").pack()
            return

        for item in cart.items:
            frame = tk.Frame(cart_frame, bg="#fdfdfd", bd=1, relief="groove")
            frame.pack(fill="x", padx=5, pady=3)

            tk.Label(frame, text=f"{item.product.name} x{item.quantity} - KES {item.subtotal()}",
                     bg="#fdfdfd", anchor="w").pack(side="left", padx=10)

            def remove_item(name=item.product.name):
                cart.remove_item(name)
                refresh_cart()

            tk.Button(frame, text="Remove", command=remove_item, bg="red", fg="white").pack(side="right", padx=10)

        total = cart.total_price()
        tk.Label(cart_frame, text=f"Total: KES {total}", bg="#ffffff", font=("Arial", 11, "bold")).pack(pady=5)

    # --- Checkout Button ---
    def checkout():
        if not cart.items:
            messagebox.showinfo("Cart Empty", "Please add items before checking out.")
            return
        cart.checkout()
        messagebox.showinfo("Success", "Purchase complete! Stock updated.")
        refresh_cart()

    tk.Button(window, text="Checkout", command=checkout, bg="#f57c00", fg="white").pack(pady=8)
