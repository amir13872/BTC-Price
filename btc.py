import requests

def get_bitcoin_data_with_proxy():
    # Define your proxy settings (replace with actual proxy)
    proxies = {
        "http": "http://your_proxy_address:port",  # Replace with your actual proxy address and port
        "https": "http://your_proxy_address:port",  # Replace with your actual proxy address and port
    }

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"
    # url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BTC&interval=5min&apikey=9XU3T5FFR4JAXHZX"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current_price = data['bitcoin']['usd']
        price_change_percent = data['bitcoin']['usd_24h_change']

        # Determine if the price is rising or falling
        if price_change_percent > 0:
            trend = "rising"
        else:
            trend = "falling"

        # ASCII Art for Bitcoin Logo
        bitcoin_logo = r"""
         ██████╗ ██╗     ███████╗██╗  ██╗██╗███╗   ██╗
         ██╔══██╗██║     ██╔════╝██║  ██║██║████╗  ██║
         ██████╔╝██║     █████╗  ███████║██║██╔██╗ ██║
         ██╔═══╝ ██║     ██╔══╝  ██╔══██║██║██║╚██╗██║
         ██║     ███████╗███████╗██║  ██║██║██║ ╚████║
         ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
        """

        print(bitcoin_logo)
        print(f"Current Bitcoin Price: ${current_price:.2f}")
        print(f"Price Change Percentage: {price_change_percent:.2f}% ({trend})")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

if __name__ == "__main__":
    get_bitcoin_data_with_proxy()