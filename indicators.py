import pandas_ta
import pandas


# Function to calculate a specified indicator
def calc_indicator(dataframe: pandas.Dataframe, indicator: str, params: dict) -> pandas.Dataframe:
    """
    Function to calculate a specified indicator
    :param dataframe: The dataframe to calculate the indicator for
    :param indicator: The indicator to calculate
    :param params: The parameters related to the indicator being calculated
    """
    # Calculate the indicator
    try:
        if indicator == "rsi":
            # Check that the indicator_period is in the params dictionary
            if "rsi_period" not in params:
                raise ValueError(f"The indicator_period is not in the params dictionary.")
            dataframe = calc_rsi(dataframe, indicator_period)
        else:
            raise ValueError(f"The indicator {indicator} is not supported.")
    except Exception as exception:
        print(f"An exception occurred in the function calc_indicator() with the indicator={indicator} and indicator_period={indicator_period}: {exception}")
        raise exception

    # Return the dataframe with the indicator values
    return dataframe

# Function to calculate the RSI
def calc_rsi(dataframe: pandas.Dataframe, rsi_period: int) -> pandas.Dataframe:
    """
    Function to calculate the RSI
    :param dataframe: The dataframe to calculate the RSI for
    :param rsi_period: The period to calculate the RSI over
    """
    # Calculate the RSI
    try:
        rsi = pandas_ta.rsi(dataframe["candle_close"], length=rsi_period)
    except Exception as exception:
        print(f"An exception occurred in the function calc_rsi() with the rsi_period={rsi_period}: {exception}")
        raise exception

    # Create a column name for the RSI
    rsi_column_name = f"rsi_{rsi_period}"

    # Concatenate the RSI values to the dataframe
    dataframe[rsi_column_name] = rsi

    # Return the dataframe with the RSI values
    return dataframe
