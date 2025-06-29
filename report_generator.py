import requests
import pandas as pd
from datetime import datetime
import os
from config import OUTPUT_DIR, API_URL, PARAMS

os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_and_save():
    response = requests.get(API_URL, params=PARAMS)
    data = response.json()

    df = pd.DataFrame(data)
    df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]

    # Add timestamp

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"crypto_report_{timestamp}.csv"
    output_path = os.path.join(OUTPUT_DIR, filename)

    df.to_csv(output_path, index=False)
    print(f"Report saved to {output_path}")


if __name__ == "__main__":
    fetch_and_save()
