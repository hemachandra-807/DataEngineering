import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
from tabulate import tabulate  # For printing tables on terminal

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'port': 3307,
    'password': 'root',
    'database': 'stock_analysis'
}

# Create the SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
conn = engine.connect()

# Create stock_data table
conn.execute(text("""
    CREATE TABLE IF NOT EXISTS stock_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ticker VARCHAR(10),
        date DATE,
        open_price DECIMAL(10, 2),
        high_price DECIMAL(10, 2),
        low_price DECIMAL(10, 2),
        close_price DECIMAL(10, 2),
        volume INT
    )
"""))

# Create company_metadata table
conn.execute(text("""
    CREATE TABLE IF NOT EXISTS company_metadata (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ticker VARCHAR(10),
        company_name VARCHAR(100),
        exchange VARCHAR(50),
        industry VARCHAR(50),
        products JSON
    )
"""))

# Load data from JSON into DB
def load_data_into_db():
    with open('stock_data.json', 'r') as f:
        stock_data = json.load(f)

    with open('company_metadata.json', 'r') as f:
        company_metadata = json.load(f)

    for record in stock_data:
        conn.execute(text("""
            INSERT INTO stock_data (ticker, date, open_price, high_price, low_price, close_price, volume)
            VALUES (:ticker, :date, :open_price, :high_price, :low_price, :close_price, :volume)
        """), {
            'ticker': record['ticker'],
            'date': record['date'],
            'open_price': record['open'],
            'high_price': record['high'],
            'low_price': record['low'],
            'close_price': record['close'],
            'volume': record.get('volume', 0)
        })

    for company in company_metadata:
        ticker = company.get('ticker')
        if not ticker:
            print(f"Warning: Missing ticker for company {company.get('company_name', 'Unknown')}. Skipping.")
            continue
        conn.execute(text("""
            INSERT INTO company_metadata (ticker, company_name, exchange, industry, products)
            VALUES (:ticker, :company_name, :exchange, :industry, :products)
        """), {
            'ticker': ticker,
            'company_name': company['company_name'],
            'exchange': company['exchange'],
            'industry': company['industry'],
            'products': json.dumps(company['products'])
        })

# Analyze stock data
def analyze_stock_data(ticker):
    query = f"SELECT * FROM stock_data WHERE ticker = '{ticker}'"
    df = pd.read_sql(query, conn)
    if df.empty:
        print(f"No data found for ticker {ticker}.")
        return
    df['date'] = pd.to_datetime(df['date'])
    print("\nStock Data (Table Format):")
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='date', y='close_price')
    plt.title(f'{ticker} Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Insert new stock manually
def insert_new_stock():
    try:
        ticker = input("Enter Ticker: ").upper()
        date = input("Enter Date (YYYY-MM-DD): ")
        open_price = float(input("Enter Open Price: "))
        high_price = float(input("Enter High Price: "))
        low_price = float(input("Enter Low Price: "))
        close_price = float(input("Enter Close Price: "))
        volume = int(input("Enter Volume: "))

        conn.execute(text("""
            INSERT INTO stock_data (ticker, date, open_price, high_price, low_price, close_price, volume)
            VALUES (:ticker, :date, :open_price, :high_price, :low_price, :close_price, :volume)
        """), {
            'ticker': ticker,
            'date': date,
            'open_price': open_price,
            'high_price': high_price,
            'low_price': low_price,
            'close_price': close_price,
            'volume': volume
        })
        print("New stock data inserted successfully.")
    except Exception as e:
        print("Failed to insert stock data:", e)

# Update existing stock
def update_stock_data(stock_id, new_close_price):
    try:
        conn.execute(text("""
            UPDATE stock_data
            SET close_price = :close_price
            WHERE id = :stock_id
        """), {
            'close_price': new_close_price,
            'stock_id': stock_id
        })
        print("Stock data updated successfully.")
    except Exception as e:
        print("Failed to update stock data:", e)

# Delete stock by ID
def delete_stock_data(stock_id):
    try:
        conn.execute(text("""
            DELETE FROM stock_data
            WHERE id = :stock_id
        """), {'stock_id': stock_id})
        print("Stock data deleted successfully.")
    except Exception as e:
        print("Failed to delete stock data:", e)

# Load data initially
load_data_into_db()

# Interactive Menu
while True:
    print("\n--- STOCK ANALYSIS MENU ---")
    print("1. Fetch and Analyze Stock")
    print("2. Insert New Stock Data")
    print("3. Update Stock Data")
    print("4. Delete Stock Data")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        # Show available tickers before asking
        result = conn.execute(text("SELECT DISTINCT ticker FROM stock_data"))
        tickers = [row[0] for row in result]
        
        if not tickers:
            print("No stock tickers available in the database.")
        else:
            print("\nAvailable Tickers:")
            print(", ".join(tickers))

            ticker = input("Enter stock ticker to analyze: ").upper()
            if ticker in tickers:
                analyze_stock_data(ticker)
            else:
                print("Invalid ticker selected.")

    elif choice == '2':
        insert_new_stock()

    elif choice == '3':
        try:
            stock_id = int(input("Enter Stock ID to update: "))
            new_price = float(input("Enter new Close Price: "))
            update_stock_data(stock_id, new_price)
        except Exception as e:
            print("Invalid input:", e)

    elif choice == '4':
        try:
            stock_id = int(input("Enter Stock ID to delete: "))
            delete_stock_data(stock_id)
        except Exception as e:
            print("Invalid input:", e)

    elif choice == '5':
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# Close connection at the end
conn.close()
