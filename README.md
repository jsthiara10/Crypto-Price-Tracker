# 🪙 Crypto Price Tracker

This is a lightweight data engineering project that automates the retrieval of cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/en/api), processes it using `pandas`, and stores it either as a timestamped CSV file or inserts it into a local SQLite database. The job is automatically scheduled to run every day at 7:30 AM using `cron`.

---

## 🚀 Features

- Pulls the top 10 cryptocurrencies by market cap via CoinGecko
- Stores output in a `/reports/` folder or SQLite database
- Auto-generates timestamped output filenames or table names
- Cron-based scheduling (runs daily at 07:30)
- Integrated test suite with GitHub Actions CI
- Built in a Python virtual environment for portability and reproducibility

---

## 📁 Project Structure

Under Construction
