# MyCrochet Haven

## Project Description  
MyCrochet Haven is a desktop-based shopping application that allows users to browse and simulate purchasing handmade crochet products. Built using Python and Tkinter, it offers a user-friendly interface where buyers can view product details, filter items by category, and manage a simple shopping cart. The application is structured using Object-Oriented Programming (OOP) principles to separate data logic, user interface, and cart management.

## Problem Solved  
Many small crochet businesses struggle to present their products digitally. MyCrochet Haven offers a virtual storefront simulation that allows customers to explore and select items in an organized and intuitive way — providing a stepping stone toward real e-commerce capabilities.

## Core Features Implemented

### 1. Product Browsing
- Displays all available crochet products with name, category, price, and stock.
- Allows filtering by product category (e.g., Wearables, Accessories, Home Décor).
- Visually indicates if an item is out of stock.

### 2. Shopping Cart (Simulated)
- Add selected products to a cart with specified quantity.
- View cart contents and the total price.
- Remove items from the cart.
- Checkout simulates a sale by reducing product stock and recording the purchase.

### 3. Data Handling
- Loads product data from `products.csv`.
- After checkout, updates stock and appends the transaction to `sales.csv`.

### 4. User Interface (GUI)
- Built using Tkinter with a clean and welcoming layout.
- Separate views for browsing products and managing the shopping cart.
- Category dropdown and action buttons are clearly placed for ease of navigation.

### 5. Object-Oriented Design
- Core classes: `Product`, `CartItem`, `Cart`.
- Applies encapsulation, modularity, and abstraction.

## Technologies / Concepts Used
- Python (functions, classes, conditionals, lists, etc.)
- Tkinter (GUI)
- `csv` module (data persistence)
- Object-Oriented Programming (OOP)

## Success Criteria (Met)
- Products load correctly from file and are displayed in the GUI.
- Users can select products and manage their cart.
- Category filter functions correctly.
- Cart totals are accurate.
- Checkout updates product stock and logs sales.
- Code is clean, modular, and follows OOP structure.

## Stretch Goals (Not Yet Implemented)
- Product popularity visualization using charts
- Crochet care tips section or "About" window
- User login/profile simulation
- Printable cart receipt or order summary

## Sample File Formats

**products.csv**
```csv
name,category,price,stock,description
Crochet Hat,Wearables,500,10,Warm and cozy handmade hat
Coaster Set,Home Décor,300,15,Colorful coasters for cups
Scrunchie,Accessories,150,25,Soft and stretchy hair scrunchie
