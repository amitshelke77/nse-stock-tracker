import yfinance as yf
import requests
import datetime
import logging
from typing import Optional
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("stock_tracker.log", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

class NSEStockTracker:
    NSE_URL = "https://www.nseindia.com/api/quote-equity?symbol="
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        self._refresh_cookies()
    
    def _refresh_cookies(self) -> None:
        try:
            self.session.get("https://www.nseindia.com", timeout=10)
            logger.info("Successfully refreshed NSE session cookies")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to refresh cookies: {e}")
    
    def is_market_open(self) -> bool:
        now = datetime.datetime.now()
        market_open = now.replace(hour=9, minute=15, second=0)
        market_close = now.replace(hour=15, minute=30, second=0)
        return market_open <= now <= market_close
    
    def get_live_price(self, symbol: str) -> Optional[float]:
        url = self.NSE_URL + symbol.upper()
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if "priceInfo" in data and "lastPrice" in data["priceInfo"]:
                price = round(float(str(data["priceInfo"]["lastPrice"]).replace(",", "")), 2)
                logger.info(f"Live price for {symbol}: Rs.{price}")
                return price
        except requests.exceptions.RequestException as e:
            logger.warning(f"Failed to fetch live price from NSE for {symbol}, switching to yfinance: {e}")
        return None
    
    def get_last_traded_price(self, symbol: str) -> Optional[float]:
        try:
            stock = yf.Ticker(symbol + ".NS")
            data = stock.history(period="1d")
            if not data.empty:
                last_price = round(data["Close"].iloc[-1], 2)
                logger.info(f"Last traded price for {symbol}: Rs.{last_price}")
                return last_price
        except Exception as e:
            logger.error(f"Failed to fetch last traded price for {symbol}: {e}")
        return None

def main():
    tracker = NSEStockTracker()
    while True:
        print("\n" + "="*50)
        print(" " * 15 + "NSE STOCK PRICE TRACKER")
        print("="*50)
        print("1. Get Live Price (Market Hours)")
        print("2. Get Last Traded Price")
        print("3. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            symbol = input("Enter NSE stock symbol (e.g., RELIANCE): ").strip().upper()
            price = tracker.get_live_price(symbol)
            if price:
                print(f"Live price of {symbol}: Rs.{price}")
            else:
                print("Failed to fetch live price. Please try again later.")
        elif choice == "2":
            symbol = input("Enter NSE stock symbol (e.g., RELIANCE): ").strip().upper()
            price = tracker.get_last_traded_price(symbol)
            if price:
                print(f"Last traded price of {symbol}: Rs.{price}")
            else:
                print("Failed to fetch last traded price. Please try again later.")
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
