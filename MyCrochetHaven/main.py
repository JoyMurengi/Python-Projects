import tkinter as tk
import random
from models import Product
from view_store import open_product_window
from purchase_window import open_cart_window


def main():
    root = tk.Tk()
    root.title("MyCrochet Haven")
    root.geometry("420x470")
    root.configure(bg="#fef9f4")  # Soft background

    # App title
    tk.Label(
        root,
        text="MyCrochet Haven",
        font=("Georgia", 16, "bold"),
        bg="#fef9f4",
        fg="#5d3a00"
    ).pack(pady=20)

    # Load all products and show pick of the day
    products = Product.load_all()
    if products:
        pick = random.choice(products)
        tk.Label(
            root,
            text=f"Pick of the Day: {pick.name} - KES {pick.price}",
            font=("Arial", 12),
            bg="#fef9f4",
            fg="#b35c00"
        ).pack(pady=5)

    # View products button
    tk.Button(
        root,
        text="Browse Products",
        command=open_product_window,
        width=22,
        height=2,
        bg="#a4c639",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=10)

    # Shop now button (cart)
    tk.Button(
        root,
        text="Shop Now",
        command=open_cart_window,
        width=22,
        height=2,
        bg="#f57c00",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=10)

    # Crochet Tip
    tips = [
        "Tip: Use cotton yarn for durability and comfort.",
        "Did you know? Crochet can reduce stress and anxiety.",
        "Care Tip: Hand-wash crochet items to avoid stretching."
    ]
    tk.Label(
        root,
        text=random.choice(tips),
        font=("Arial", 10, "italic"),
        bg="#fef9f4",
        fg="#444"
    ).pack(pady=15)

    # Exit button
    tk.Button(
        root,
        text="Exit",
        command=root.destroy,
        width=22,
        height=1,
        bg="gray",
        fg="white"
    ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
