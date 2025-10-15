# Jumia-Scraper
# Jumia Kenya "Deals of the Week" Scraper

This project scrapes the **"Deals of the Week"** section from the [Jumia Kenya](https://www.jumia.co.ke/) homepage using Python.  
It extracts product details such as name, brand, price, discount, reviews, and rating, and calculates a **popularity score**, then saves the results into a CSV file.

---

## Overview

Many online stores do not provide APIs for quick data extraction.  
This script uses **web scraping** to automatically collect product data from Jumia Kenya for analysis or reporting purposes.

The project demonstrates:
- Sending HTTP requests  
- Parsing HTML with BeautifulSoup  
- Extracting and cleaning data  
- Saving results to a CSV file for analysis

---

## Features

- Accesses the Jumia Kenya homepage  
- Finds and scrapes products in the **"Deals of the Week"** section  
- Extracts:
  - Product Name  
  - Brand (first word of name)  
  - Price (in KSh)  
  - Discount (%)  
  - Reviews (count)  
  - Rating (out of 5)  
- Calculates a **popularity score** as:  
Popularity = (reviews + 1) * (rating + 1)

## Limitations
- The scraper only captures data from the homepage "Deals of the Week" section.  
- Some product names or reviews may be missing due to Jumia’s HTML structure.  
- Jumia’s website layout may change, requiring small code updates.

---

## Future Improvements
- Implement pagination to scrape more products.  
- Clean and standardize product names.  
- Add data visualization for top deals or best discounts.  
- Automate daily scraping with a scheduler.

