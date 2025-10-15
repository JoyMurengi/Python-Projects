# main.py

import requests
from bs4 import BeautifulSoup
import csv
import re

# Step 1: Set up URL and headers
url = "https://www.jumia.co.ke/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Step 2: Send HTTP request
response = requests.get(url, headers=headers)

# Step 3: Check status code
if response.status_code != 200:
    print(" Failed to access Jumia. Status code:", response.status_code)
    exit()
else:
    print("Successfully accessed Jumia Kenya")

# Step 4: Parse the homepage content
soup = BeautifulSoup(response.content, "html.parser")

# Step 5: Find product containers in the "Deals of the Week" section
products = soup.find_all("article", class_="prd")

print(f"Found {len(products)} products.")

# Step 6: Extract required product details
data = []

for product in products:
    # i) Product Name
    name_tag = product.find("h3", class_="name")
    name = name_tag.text.strip() if name_tag else "No name"

    # ii) Brand Name (from product name)
    brand = name.split()[0] if name != "No name" else "Unknown"

    # iii) Price (Ksh)
    price_tag = product.find("div", class_="prc")
    price = price_tag.text.strip().replace("Ksh", "") if price_tag else "N/A"

    # iv) Discount if available
    discount_tag = product.find("div", class_="bdg _dsct")
    discount = discount_tag.text.strip().replace("-", "") if discount_tag else "0%"

    # v) Total Number of Reviews
    reviews_tag = product.find("div", class_="rev")
    reviews_text = reviews_tag.text.strip() if reviews_tag else "0"
    reviews = int(re.findall(r'\d+', reviews_text)[0]) if re.findall(r'\d+', reviews_text) else 0

    # vi) Product Rating (out of 5)
    rating_tag = product.find("div", class_="stars _s")
    if rating_tag and rating_tag.get("aria-label"):
        match = re.search(r'(\d+(\.\d+)?)', rating_tag.get("aria-label"))
        rating = float(match.group()) if match else 0.0
    else:
        rating = 0.0

    # Popularity Score = (reviews + 1) * (rating + 1)
    popularity_score = (reviews + 1) * (rating + 1)

    data.append([name, brand, price, discount, reviews, rating, round(popularity_score, 2)])

# Step 7: Save scraped data to CSV
with open("jumia_deals.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Brand", "Price (Ksh)", "Discount (%)", "Reviews", "Rating", "Popularity Score"])
    writer.writerows(data)

print(" Data saved to 'jumia_deals.csv'")
