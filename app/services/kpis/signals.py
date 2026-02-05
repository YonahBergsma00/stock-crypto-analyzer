import pandas as pd

def rsi_signal(rsi:float) -> str:
    if rsi >= 70:
        return "Overbought"
    elif rsi <= 30:
        return "Oversold"
    return "Neutral"


def trend_signal(trend_dict: dict) -> str:
    """
    Convert SMA trend into a simple signal.
    """
    trend = trend_dict["trend"]
    strength = trend_dict["trend_val"]

    if trend == "Uptrend" and strength > 2:
        return "Bullish"
    elif trend == "Uptrend" and strength <= 2:
        return "Neutral/Bullish"
    elif trend == "Downtrend" and strength < -2:
        return "Bearish"
    else:
        return "Neutral"


def sma_crossover(prices:pd.Series, ticker: str, short_window: int = 20, long_window: int = 50) -> str:
    
    sma_short = prices.rolling(window=short_window).mean()
    sma_long = prices.rolling(window=long_window).mean()

    # yesterday vs today
    if sma_short[ticker].iloc[-2] < sma_long[ticker].iloc[-2] and sma_short[ticker].iloc[-1] > sma_long[ticker].iloc[-1]:
        return "Golden Cross"
    elif sma_short[ticker].iloc[-2] > sma_long[ticker].iloc[-2] and sma_short[ticker].iloc[-1] < sma_long[ticker].iloc[-1]:
        return "Death Cross"
    else:
        return "None"