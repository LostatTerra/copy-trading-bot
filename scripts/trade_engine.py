import time

def connect_to_broker():
    # Placeholder: Later this will connect to Alpaca or Kraken
    print("Connecting to broker...")

def fetch_signals():
    # Placeholder: Pretend to fetch trades
    print("Fetching latest trades...")
    return [{"symbol": "BTCUSD", "action": "buy", "amount": 10}]

def execute_trade(trade):
    print(f"Executing {trade['action']} order for {trade['symbol']} - Amount: {trade['amount']}")

def main():
    connect_to_broker()
    trades = fetch_signals()
    for trade in trades:
        execute_trade(trade)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)  # Wait 60 seconds before checking again
