import yfinance as yf
import pandas as pd

def get_historical_prices(
        ticker: str,
        period: str="6mo",
        interval: str="1d",
) -> pd.Series:
    """
    Fetch historical close prices for a ticker.
    Works both for stocks and crypto.
    """

    data = yf.download(
        ticker,
        period=period,
        interval=interval,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No data found for ticker {ticker}")
    
    return data["Close"]