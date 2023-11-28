import alpaca_interactions as alpaca


# Function to get market data
def get_market_data(symbol: str, timeframe: str, limit: int, start_date: datetime, end_date: datetime) -> pandas.Dataframe:
    """
    Function to get market data
    :param symbol: The symbol to get market data for
    :param timeframe: The timeframe to get market data for
    :param limit: The number of bars to get
    :param start_date: The start date to get market data for
    :param end_date: The end date to get market data for
    """
    # Get the market data
    market_data = alpaca.get_historic_bars(
        symbols=[symbol], 
        timeframe=timeframe, 
        limit=limit, 
        start_date=start_date, 
        end_date=end_date
    )

    # Return the market data
    return market_data
