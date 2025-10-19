"""
price_check.py
---------------
Fetches and displays the latest stock prices for a predefined list of symbols 
using the Alpaca Market Data API.

Usage:
    python -m alpaca_trading.scripts.price_check
"""

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca_trading.config.keys import load_api_keys
from tabulate import tabulate

def main():
    API_KEY, API_SECRET = load_api_keys()
    data_client = StockHistoricalDataClient(API_KEY, API_SECRET)

    symbols = ["SPY", "VOO", "HOOD", "TSM", "AMZN", "GOOGL"]
    price_table = [["Symbol", "Price"]]

    for sym in symbols:
        try:
            latest_quote = data_client.get_stock_latest_quote(StockLatestQuoteRequest(symbol_or_symbols=sym))
        except Exception as e:
            print(f"An error occurred: {e}")
        price_table.append([sym, latest_quote[sym].ask_price])

    print(tabulate(price_table, headers="firstrow", tablefmt="orgtbl")+"\n")


if __name__ =="__main__":
    main()