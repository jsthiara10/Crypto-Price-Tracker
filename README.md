# 📈 Crypto Price Tracker

A lightweight, automated data pipeline that retrieves real-time cryptocurrency market data from the CoinGecko API, transforms it using `pandas`, and stores clean, timestamped CSV reports — all scheduled to run daily via `cron`.

---

## ⚙️ Overview

This project demonstrates best practices in data engineering on a small scale — combining **API ingestion**, **modular data pipelines**, and **automated reporting**. Built in a Python virtual environment for full reproducibility.

---

## 🚀 Features

- 🔁 **Modular ETL Pipeline**:
- 
  Clean separation of concerns across Extract, Transform, and Load stages using custom Python classes.

- 📊 **Top 50 Cryptos Tracked**  
  Pulls live (at-time) market data for the top 50 cryptocurrencies by market cap.

- 🧹 **Data Cleaning with `pandas` & Regex**  
  - Filters and selects only the most relevant columns  
  - Standardises column names using regex and string manipulation  
  - Ensures consistent, analysis-ready formatting

- 📁 **Auto-Saved Reports**  
  - Saves outputs as timestamped `.csv` files in the `/reports/` folder  
  - Ensures easy historical tracking of daily snapshots

- ⏰ **Daily Scheduling via Cron**  
  Automates the ETL job to run every morning at 07:30

- ✅ **CI Testing with GitHub Actions**  
  Integrated test suite for reliability and continuous integration

---

## 🔍 High-Level Technical Breakdown

**🔌 Data Extraction:**

The requests library makes an HTTP GET request to the CoinGecko API, passing in custom parameters (like sorting by market cap). The API returns JSON, which is immediately converted into a pandas.DataFrame for analysis.

**🧼 Data Transformation (Cleaning):**

The transformer uses a pipeline of **pure functions** to clean the data

**Column Filtering:** Only essential fields like price, volume, and percentage change are retained.

**Regex-Like Normalisation:** While not using raw regex, column names are programmatically "cleaned" by capitalising each word and removing underscores — mimicking what a regex cleanup would do.

**Extensibility:** New transformations can be easily added by appending to the .steps list in the CryptoTransformer class.

**💾 Data Loading (Storage):**
The cleaned DataFrame is saved to disk as a CSV using pandas.to_csv(), with a timestamped filename. The os.makedirs() call ensures the output directory exists before saving.

**🧪 Testable & Modular Design:**
Each step of the ETL process is encapsulated in its own class, making it easy to mock, test, or replace. External dependencies like the API and file system are isolated for clean unit testing.




---

## 📂 Project Structure

````
Crypto-Price-Tracker/
├── crypto_tracker/
│ ├── main.py # Entry point
│ ├── report_generator.py # ETL pipeline
│ ├── config.py # Config constants
│ └── init.py
├── reports/ # Auto-generated CSV reports
├── tests/ # Unit tests
├── .github/workflows/ # GitHub Actions CI config
├── venv/ # Python virtual environment
└── requirements.txt
````


---

## 🛠️ Technologies Used

- Python 3
- `pandas` for data wrangling  
- `requests` for API communication  
- `cron` for scheduling  
- GitHub Actions for CI

---

## ✅ Setup Instructions - Mac/Linux (Windows coming soon!)

1. **Clone the repo**  
   ```bash
   git clone https://github.com/jsthiara10/Crypto-Price-Tracker.git
   cd Crypto-Price-Tracker

2. **Set up the Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
   
3. **Run the pipeline manually**

    ```bash
   ./venv/bin/python -m crypto_tracker.main

4. **Add crontab or daily automation - RECOMMENDED**

The goal is to schedule your script to run every day at a specific time **(e.g. 7:30AM)**

**Open your crontab**

```bash
crontab -e
```

**Add the cron job (example uses time of 7:30AM)**

```bash
30 7 * * * /absolute/path/to/venv/bin/python /absolute/path/to/Crypto-Price-Tracker/crypto_tracker/main.py >> /absolute/path/to/Crypto-Price-Tracker/cron.log 2>&1
```
**Save and exit**
```
In nano: Press Ctrl + X, then Y, then Enter

In vim: Press Esc, then type :wq, then Enter
```

**Verify cron is active**

```bash
crontab -l
```

## 🧪 Unit Testing

This project includes unit tests for the ETL pipeline components (extractor, transformer, and loader). Tests are written using pytest and are located in the tests/ directory.

**✅ How to Run Tests**

Activate your virtual environment (if not already):

```bash
source venv/bin/activate
```

**Install testing dependencies**

```bash
pip install pytest
```

**Run all tests**

```bash
pytest
````

**Alternatively, run tests inside the tests/ folder explicitly**

```bash
pytest tests/
```

## 🚀 Future Plans

**📂 Multiple Output Formats**

Extend support beyond CSV to:

.xlsx Excel reports (using pandas.ExcelWriter)

SQLite or PostgreSQL databases for structured querying

**☁️ Cloud-Based Deployment**

Adapt the ETL pipeline for cloud environments (e.g., AWS Lambda, GCP Cloud Functions, or Docker + scheduled jobs on EC2), enabling:

Off-device scheduling

Remote storage (S3, GCS, or Azure Blob)

**📊 Historical Data Archiving**

Store and compare past reports to enable basic trend and volatility analysis.

**🧪 Integration Tests**

Implement end-to-end testing for the entire ETL workflow.

**🔌 API Flexibility**
Add support for alternative data providers (e.g., CoinMarketCap, CryptoCompare).

**🖥 Platform Compatibility**

Finalise support and setup instructions for Windows and Linux systems.




