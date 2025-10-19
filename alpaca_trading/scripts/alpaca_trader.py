"""
alpaca_trader.py

Simple Python script to place paper trading buy or sell orders
via the Alpaca API. Prompts the user for a stock symbol, action
(BUY/SELL), and quantity, then submits a market order.

Usage:
    python -m alpaca_trading.scripts.alpaca_trader
"""

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca_trading.config.keys import load_api_keys

API_KEY, API_SECRET = load_api_keys()
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)

def main():
    symbol = input("Enter stock symbol: ").upper().strip()
    action = input("Buy or Sell: ").strip().upper()
    qty = int(input("Number of shares: "))

    market_order = place_trade(trading_client, symbol, qty, action)
    print(f"Order submitted: {market_order}")

def place_trade(trading_client, symbol, qty, action):
    if action not in ["BUY", "SELL"]:
        raise ValueError("Action must be 'BUY' or 'SELL'")

    market_order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY if action == "BUY" else OrderSide.SELL,
        time_in_force=TimeInForce.DAY
    )

    market_order = trading_client.submit_order(order_data=market_order_data)
    return market_order

if __name__ == "__main__":
    main()
