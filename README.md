# BTC-Price
# Writing the README content into a file named "README.md"

readme_content = """
# README for **Bitcoin Data Fetcher**

---

## **Introduction**  
This script allows you to fetch real-time Bitcoin price data from the CoinGecko API. It also displays the 24-hour percentage price change and includes support for using a proxy for enhanced security or bypassing access restrictions.

---

## **Features**  
- **Real-time Bitcoin Price**: Fetch up-to-date Bitcoin price in USD.  
- **24-Hour Price Change**: View percentage increase or decrease in the last 24 hours.  
- **Proxy Compatibility**: Configure a proxy for secure and unrestricted access.  
- **Simple and Clear Output**: Includes ASCII art of the Bitcoin logo for a fun, readable display.  

---

## **Requirements**  
- Python 3.6 or above  
- `requests` library (Install with: `pip install requests`)  

---

## **How to Use**  
### **Steps**  
1. Download or copy the script.  
2. Open the script in your Python environment.  
3. To use a proxy, replace the placeholder with your proxy details in the code:  
   ```python
   proxies = {
       "http": "http://your_proxy_address:port",
       "https": "http://your_proxy_address:port",
   }
