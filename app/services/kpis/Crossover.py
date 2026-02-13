import pandas as pd

def calculate_crossover(prices: pd.Series, ticker: str, short_window: int = 20, long_window: int= 50) -> dict:
    """
    Returns latest, mean, and std of crossover strength series
    """
    # Calculate SMAs
    sma_short = prices.rolling(window=short_window).mean()
    sma_long = prices.rolling(window=long_window).mean()

    # Continuous strength series
    strength_series = (sma_short[ticker] - sma_long[ticker]) / sma_long[ticker]

    latest_strength = strength_series.iloc[-1]
    mean_strength = strength_series.mean()
    std_strength = strength_series.std()

    return {
        "latest": float(latest_strength),
        "mean": float(mean_strength),
        "std": float(std_strength)
    }