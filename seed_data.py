import mysql.connector
import random
from datetime import datetime, timedelta

# --- CONFIGURATION ---
db_config = {
    "host": "localhost",
    "user": "root", 
    "password": "TheWhi994$|$9lDB", # <--- UPDATE THIS
    "database": "minimart_db"
}

try:
    print("Connecting to database...")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Setup data options
    products = [
        ('Chips', 1.50), 
        ('Soda', 1.00), 
        ('Candy', 0.75), 
        ('Sandwich', 4.50), 
        ('Coffee', 2.00), 
        ('Energy Drink', 3.00),
        ('Bread', 2.50)
    ]

    print("Generating 1,000 random sales...")

    sql = "INSERT INTO sales (product_name, quantity, price_per_unit, sale_date) VALUES (%s, %s, %s, %s)"
    val_list = []

    start_date = datetime(2023, 1, 1)

    for _ in range(1000):
        # Pick a random product
        prod = random.choice(products)
        name = prod[0]
        price = prod[1]
        
        # Pick random quantity (1 to 5)
        qty = random.randint(1, 5)
        
        # Pick random date within 365 days
        random_days = random.randint(0, 365)
        date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        val_list.append((name, qty, price, date))

    # --- THE FIX IS HERE ---
    print("Inserting data...")
    cursor.executemany(sql, val_list)  # Must be executemany, not execute!
    
    conn.commit()
    print(f"Success! {cursor.rowcount} sales inserted.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")