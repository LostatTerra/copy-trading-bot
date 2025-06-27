import time
import os
import alpaca_trade_api as tradeapi

def connect_to_broker():
    # Pull your API keys from GitHub Actions secrets
    api_key = os.getenv("ALPACA_API_KEY")
    secret_key = os.getenv("ALPACA_SECRET_KEY")
    base_url = "https://paper-api.alpaca.markets"

    if not api_key or not secret_key:
        raise Exception("Missing Alpaca API credentials.")

    api = tradeapi.REST(api_key, secret_key, base_url, api_version='v2')
    print("✅ Connected to Alpaca Paper Trading")
    return api

def fetch_account(api):
    account = api.get_account()
    print(f"💰 Cash balance: ${account.cash}")
    return account

def main():
    try:
        api = connect_to_broker()
        fetch_account(api)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
