# BTC-Price

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
   ```
4.Run the script: 
```
python btc.py
```

---

## **Sample Output**
When executed successfully, the script will display information like this:

```
 ██████╗ ██╗     ███████╗██╗  ██╗██╗███╗   ██╗
 ██╔══██╗██║     ██╔════╝██║  ██║██║████╗  ██║
 ██████╔╝██║     █████╗  ███████║██║██╔██╗ ██║
 ██╔═══╝ ██║     ██╔══╝  ██╔══██║██║██║╚██╗██║
 ██║     ███████╗███████╗██║  ██║██║██║ ╚████║
 ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

Current Bitcoin Price: $xxxxx.xx  
Price Change Percentage: xx.xx% (rising/falling)
```

---

## **Customization**
- Modify the API URL to fetch data from other sources.
- Enhance proxy settings for advanced security features.

---

## **License**
This project is licensed under the MIT License. You are free to use and modify it as needed.

---

## **Feedback and Contributions**  
We welcome your feedback and contributions! If you have ideas to improve the script or encounter issues, feel free to:  

1. **Open an Issue**: Report bugs or suggest features.  
2. **Submit a Pull Request**: Contribute directly to the codebase.  
3. **Contact Us**: Email us at [Amir Mahdi Zare](mailto:mahnaznamani007@gmail.com).  

Your feedback is invaluable and helps us make this project even better!
