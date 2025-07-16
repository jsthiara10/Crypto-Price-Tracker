import requests
import pandas as pd
from datetime import datetime
import os
from crypto_tracker.config import OUTPUT_DIR, API_URL, PARAMS

os.makedirs(OUTPUT_DIR, exist_ok=True)


class CryptoExtractor:
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def fetch(self):
        response = requests.get(self.url, params=self.params)
        data = response.json()
        return pd.DataFrame(data)


class CryptoTransformer:
    def __init__(self):
        self.steps = [self.select_columns, self.normalise_column_names]

    def transform(self, df):
        for step in self.steps:
            df = step(df)
        return df

    def select_columns(self, df):
        selected = [
            "id", "symbol", "name", "current_price",
            "market_cap", "total_volume", "price_change_percentage_24h"
        ]
        return df[selected]

    def normalise_column_names(self, df):
        df.columns = [
            "_".join([word.capitalize() for word in col.split("_")])
            for col in df.columns
        ]
        return df


class CryptoLoader:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def save(self, df):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"crypto_report_{timestamp}.csv"
        path = os.path.join(self.output_dir, filename)
        df.to_csv(path, index=False)
        print(f"✅ Report saved to {path}")


def run_etl():
    extractor = CryptoExtractor(API_URL, PARAMS)
    transformer = CryptoTransformer()
    loader = CryptoLoader(OUTPUT_DIR)

    df = extractor.fetch()
    df = transformer.transform(df)
    loader.save(df)


if __name__ == "__main__":
    run_etl()
