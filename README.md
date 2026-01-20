# 🛒 Mini-Mart Sales Analysis

## 📌 Project Overview
This project analyzes sales data for a local convenience store to identify top-selling products and monthly revenue trends. The goal is to help the business owner optimize inventory and understand seasonal sales patterns.

## 📊 Key Insights
* **Top Performer:** "Sandwiches" are the highest revenue driver, generating nearly 2x the revenue of the next best product.
* **Sales Stability:** Sales remained consistent (approx $400-$600/month) throughout 2023.
* **Inventory Recommendation:** Prioritize stock for Sandwiches and Energy Drinks, as they account for >40% of total revenue.

## 🛠️ Tech Stack
* **Python:** Data extraction, cleaning, and visualization.
* **MySQL:** Relational database for storing transaction records.
* **Pandas & Matplotlib:** Data manipulation and plotting.

## 📂 Project Structure
* `seed_data.py`: A script that generates 1,000 rows of realistic dummy data and inserts it into MySQL.
* `analysis.py`: Connects to the database, calculates KPIs, and generates visualization charts.

## 🚀 How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Setup your MySQL database using `seed_data.py`.
4.  Run the analysis: `python analysis.py`
