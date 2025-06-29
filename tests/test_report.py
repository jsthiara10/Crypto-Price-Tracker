import pytest
import requests

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 1,
    "page": 1,
    "sparkline": "false"
}

def test_api_response_status():
    response = requests.get(API_URL, params=PARAMS)
    assert response.status_code == 200

def test_api_response_fields():
    response = requests.get(API_URL, params=PARAMS)
    data = response.json()
    assert isinstance(data, list)
    assert "id" in data[0]
    assert "current_price" in data[0]