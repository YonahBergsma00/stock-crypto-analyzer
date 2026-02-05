import numpy as np
import pandas as pd

def calculate_volatility(prices: pd.Series, ticker: str, window: int = 21) -> dict:
    """
    Calculate annualized volatility based on daily returns.
    """
    # Daily returns
    daily_returns = prices.pct_change().dropna()

    # Rolling volatility (window in days)
    rolling_vol = daily_returns.rolling(window=window).std() * np.sqrt(252)

    # Latest volatility (scalar)
    latest_vol = float(round(rolling_vol[ticker].iloc[-1], 2))

    # Mean & std over the rolling volatility series (ignore NaN)
    mean_vol = float(round(rolling_vol[ticker].mean(), 2))
    std_vol = float(round(rolling_vol[ticker].std(), 2))

    return {
        "vol_val": latest_vol,
        "vol_mean": mean_vol,
        "vol_std": std_vol
    }