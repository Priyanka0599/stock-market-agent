from utils.fetch_stock_data import get_stock_data

def run_agent():
    print("Running stock agent...")
    data = get_stock_data("AAPL")
    print(data.tail())
