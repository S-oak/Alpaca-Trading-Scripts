# Alpaca Trading Scripts

A collection of Python scripts executed through the Alpaca API for testing and automating stock trades.
These scripts are designed for paper trading and experimentation.

## Requirements
Python 3.8+

Installed packages:
```bash
alpaca-trade-api
tabulate
python-dotenv
```
## Configuration
Create a .env file in the project root with your Alpaca paper trading keys:
```bash
API_KEY=your_paper_trading_key
API_SECRET=your_paper_trading_secret
```
## Usage
Run scripts as modules from the project root, for example:
```bash
python -m alpaca_trading.scripts.alpaca_trader
```
## License
Licensed under the MIT License.
