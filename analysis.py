import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
db_config = {
    "host": "localhost",
    "user": "root", 
    "password": "TheWhi994$|$9lDB", 
    "database": "minimart_db"
}

try:
    print("Connecting to MySQL...")
    conn = mysql.connector.connect(**db_config)
    
    # 1. GET DATA
    # We will use SQL to do the heavy lifting this time!
    # This queries monthly revenue directly from the DB.
    query = """
    SELECT 
        DATE_FORMAT(sale_date, '%Y-%m') as month, 
        SUM(quantity * price_per_unit) as revenue
    FROM sales
    GROUP BY month
    ORDER BY month ASC
    """
    
    print("Fetching monthly trend data...")
    df = pd.read_sql(query, conn)
    
    # 2. VISUALIZE (Line Chart)
    print("Plotting Line Chart...")
    
    plt.figure(figsize=(10, 5))  # Make the chart wider
    plt.plot(df['month'], df['revenue'], marker='o', linestyle='-', color='green', linewidth=2)
    
    plt.title('Monthly Sales Trend (2023)')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue ($)')
    plt.grid(True) # Adds a grid behind the lines
    plt.xticks(rotation=45) # Tilts the dates so they don't overlap
    
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")