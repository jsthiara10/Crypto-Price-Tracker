# tests/test_transformer.py

import pandas as pd
from crypto_tracker.report_generator import CryptoTransformer


def test_transformer_outputs_expected_columns():
    # 🧱 Sample input DataFrame with extra columns
    raw_columns = [
        "id", "symbol", "name", "current_price", "market_cap", "total_volume",
        "price_change_percentage_24h", "extra_column"
    ]
    sample_data = [{col: f"mock_{col}" for col in raw_columns}]
    df = pd.DataFrame(sample_data)

    # 🌀 Apply transformer
    transformer = CryptoTransformer()
    transformed_df = transformer.transform(df)

    # ✅ Check resulting columns match expected normalized set
    expected_cols = [
        "Id", "Symbol", "Name", "Current_Price", "Market_Cap",
        "Total_Volume", "Price_Change_Percentage_24h"
    ]
    assert list(transformed_df.columns) == expected_cols

    # 📊 Make sure row data is still intact
    assert transformed_df.shape == (1, len(expected_cols))
