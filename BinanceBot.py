import ccxt
import time

# Binance API credentials
api_key = ''
api_secret = ''

# Initialize Binance exchange
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
})

# Adjust for time difference
exchange.options['adjustForTimeDifference'] = True
exchange.load_time_difference()

# Trading parameters
symbol = 'BTC/USDT'
buy_threshold = 0.95  # Buy if price drops by 5%
sell_threshold = 1.05  # Sell if price rises by 5%
usd_amount = 10  # Amount in USD to use for each trade
check_interval = 60  # Check every 60 seconds

def get_latest_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def create_market_buy_order(symbol, usd_amount):
    price = get_latest_price(symbol)
    amount = usd_amount / price
    order = exchange.create_market_buy_order(symbol, amount)
    return order

def create_market_sell_order(symbol, usd_amount):
    price = get_latest_price(symbol)
    amount = usd_amount / price
    order = exchange.create_market_sell_order(symbol, amount)
    return order

# Initial price
initial_price = get_latest_price(symbol)

while True:
    try:
        current_price = get_latest_price(symbol)
        print(f"Current price of {symbol}: {current_price}")

        # Buy logic
        if current_price <= initial_price * buy_threshold:
            print(f"Price dropped to {current_price}, buying ${usd_amount} worth of {symbol.split('/')[0]}")
            create_market_buy_order(symbol, usd_amount)
            initial_price = current_price  # Reset initial price to current

        # Sell logic
        
        elif current_price >= initial_price * sell_threshold:
            print(f"Price rose to {current_price}, selling ${usd_amount} worth of {symbol.split('/')[0]}")
            create_market_sell_order(symbol, usd_amount)
            initial_price = current_price  # Reset initial price to current

        time.sleep(check_interval)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(check_interval)
