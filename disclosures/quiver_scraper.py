import requests
import datetime
import json

def fetch_fmp_congress_trades():
    urls = [
        "https://financialmodelingprep.com/api/v4/senate-latest",
        "https://financialmodelingprep.com/api/v4/house-latest"
    ]

    recent_trades = []
    cutoff_date = datetime.datetime.utcnow() - datetime.timedelta(days=3)

    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            continue

        for entry in data:
            try:
                ticker = entry.get("ticker")
                action = entry.get("type")  # 'Buy' or 'Sell'
                owner = entry.get("name")
                date_str = entry.get("transactionDate")
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

                if ticker and action and date >= cutoff_date:
                    recent_trades.append({
                        "ticker": ticker,
                        "action": action,
                        "owner": owner,
                        "date": date_str
                    })

            except:
                continue

    return recent_trades

if __name__ == "__main__":
    trades = fetch_fmp_congress_trades()
    print(json.dumps(trades, indent=2))
