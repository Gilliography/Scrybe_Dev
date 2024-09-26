import ccxt
import time

# Initialize exchanges with your API keys
binance = ccxt.binance({
    'apiKey': 'YOUR_BINANCE_API_KEY',
    'secret': 'kPOBmx1iMsbX01mxdPBWqhsSRFJUy43SH2MhxLBSurttlHl3ICiSfL8NfY5cgmMZ',
})

kraken = ccxt.kraken({
    'apiKey': 'YOUR_KRAKEN_API_KEY',
    'secret': 'YOUR_KRAKEN_SECRET_KEY',
})

# Define the trading pair and amount
symbol = 'BTC/USDT'
amount = 0.001  # Adjust based on your needs

def fetch_prices():
    try:
        binance_price = binance.fetch_ticker(symbol)['last']
        kraken_price = kraken.fetch_ticker('BTC/USD')['last']
        return binance_price, kraken_price
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None, None

def execute_trade(exchange, symbol, order_type, amount):
    try:
        if order_type == 'buy':
            response = exchange.create_market_buy_order(symbol, amount)
        elif order_type == 'sell':
            response = exchange.create_market_sell_order(symbol, amount)
        print(f"Executed {order_type} order: {response}")
    except Exception as e:
        print(f"Error executing trade: {e}")

def arbitrage_opportunity():
    binance_price, kraken_price = fetch_prices()
    
    if binance_price is None or kraken_price is None:
        return

    if binance_price < kraken_price:
        print(f"Arbitrage Opportunity: Buy on Binance at {binance_price} and sell on Kraken at {kraken_price}")
        execute_trade(binance, symbol, 'buy', amount)
        execute_trade(kraken, 'BTC/USD', 'sell', amount)
    elif kraken_price < binance_price:
        print(f"Arbitrage Opportunity: Buy on Kraken at {kraken_price} and sell on Binance at {binance_price}")
        execute_trade(kraken, 'BTC/USD', 'buy', amount)
        execute_trade(binance, symbol, 'sell', amount)
    else:
        print("No arbitrage opportunity found")

# Run arbitrage check periodically
while True:
    arbitrage_opportunity()
    time.sleep(60)  # Check every minute
