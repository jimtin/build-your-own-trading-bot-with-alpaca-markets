import alpaca_interactions as alpaca
import datetime
import indicators


# Function to start the trading bot
def lets_get_started():
    """
    Function to start the trading bot
    """
    print("Hello World")
    # Get the latest trade price for AAPL
    latest_trade = alpaca.get_latest_trade("AAPL")
    print(latest_trade)
    # Get a list of the last 100 bars for AAPL
    # Set the end_date to today
    end_date = datetime.datetime.now()
    # Set the start_date to 100 days ago
    start_date = end_date - datetime.timedelta(days=100)
    # Get the last 100 bars for AAPL
    bars = alpaca.get_historic_bars(
        symbols=["AAPL"], 
        timeframe="1day", 
        limit=100, 
        start_date=start_date, 
        end_date=end_date)
    print(bars)

    return


# Main function for program
if __name__ == "__main__":
    lets_get_started()
