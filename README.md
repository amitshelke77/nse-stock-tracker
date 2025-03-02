# 📈 NSE Stock Price Tracker

A Python script to fetch **live stock prices** (during market hours) and **last traded prices** (after market close) for NSE-listed stocks using **NSE API** and **yfinance**.

## 🚀 Features
- ✅ **Get Live Price** (NSE API) – Fetches real-time price when the market is open.
- ✅ **Get Last Traded Price** (yfinance) – Fetches the last available closing price.
- ✅ **Auto-Detects Market Hours** – Uses NSE API during market hours, yfinance otherwise.
- ✅ **Handles API Failures** – Falls back to yfinance if NSE API is blocked.
- ✅ **Error Handling & Logging** – Tracks requests and errors in `stock_fetcher.log`.

## 🛠️ Installation
### 1️⃣ Install Dependencies
#### Option 1: Using `requirements.txt` (Recommended)
```bash
pip install -r requirements.txt
```

#### Option 2: Manually Install Packages
```bash
pip install yfinance requests
```

### 2️⃣ Run the Script
```bash
python stock_fetcher.py
```

## 📌 Usage
1. **Run the script** and choose an option:
```
==================================================
               NSE STOCK PRICE TRACKER
==================================================
1. Get Live Price (Market Hours)
2. Get Last Traded Price
3. Exit
==================================================
```
2. **Enter stock symbol** (e.g., RELIANCE, TCS, HDFC).
3. View **real-time price** (if market open) or **last traded price** (if closed).

## 📊 Example Output
```
Enter NSE stock symbol (e.g., RELIANCE): RELIANCE
Live price of RELIANCE: Rs.1200.10
```

## 🏈 Future Enhancements
- 🔄 **Auto-Refresh Prices** every few seconds
- 📊 **Save Data to CSV** for tracking historical changes
- 📱 **Web App Integration** using Flask/Django
- 🔔 **Price Alerts & Notifications**

## 🤝 Contribute
Feel free to **fork, improve & submit a PR**! Suggestions are always welcome.

## 🐝 License
This project is **open-source** under the MIT License.

---

🚀 **Follow for more trading automation tools!**

