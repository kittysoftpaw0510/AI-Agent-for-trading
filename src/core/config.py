"""
🌙 Moon Dev's Trading Configuration
All the magic numbers and settings live here! 
Remember: Moon Dev says always be careful with your config! 🚀
"""

# Token and wallet settings
symbol = '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump'
address = '4wgfCBf2WwLSRKLef9iW7JXZ2AfkxUxGM4XcKpHm3Sin'

# Position sizing 🎯
usd_size = 5  # Size of position to hold
max_usd_order_size = 1  # Max order size
tx_sleep = 30  # Sleep between transactions
slippage = 199  # Slippage settings

# Transaction settings ⚡
slippage = 199  # 50% slippage, 500 = 5% and 50 = .5% slippage
PRIORITY_FEE = 100000  # ~0.02 USD at current SOL prices
orders_per_open = 3  # Multiple orders for better fill rates

# Market maker settings 📊
buy_under = .0946
sell_over = 1

# Risk management 🛡️
STOPLOSS_PRICE = 1
BREAKOUT_PRICE = .0001
SLEEP_AFTER_CLOSE = 600  # Prevent overtrading

# Data collection settings 📈
DAYSBACK_4_DATA = 10
DATA_TIMEFRAME = '15m'

# Future variables (not active yet) 🔮
sell_at_multiple = 3
USDC_SIZE = 1
limit = 49
timeframe = '15m'
stop_loss_perctentage = -.24
tokens_to_trade = ['777']
EXIT_ALL_POSITIONS = False
DO_NOT_TRADE_LIST = ['777']
CLOSED_POSITIONS_TXT = '777'
minimum_trades_in_last_hour = 777