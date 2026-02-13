import numpy as np

def z_score(value, mean, std):
    return (value - mean) / std if std > 0 else 0

def probability_up(kpis: dict, weights: dict, bias: float = 0.0) -> float:
    """
    Returns probability that the asset will go up (0-1) based on z-scores
    """
    linear = (
        weights['rsi'] * kpis['rsi_z'] +
        weights['trend'] * kpis['trend_z'] +
        weights['vol'] * kpis['vol_z'] +
        weights['sentiment'] * kpis['sentiment_z'] +
        weights['crossover'] * kpis['crossover_z'] +
        bias
    )
    prob = 1 /(1 + np.exp(-linear))
    return prob


def z_score_regressors(kpis: dict) -> dict:
    """
    Combine z-scores of RSI, trend, and volatility into a final score.
    weights = importance of each KPI
    Returns a value that can be interpreted as "buy strength"
    """
    rsi_z = z_score(kpis["rsi"]["rsi_val"], kpis["rsi"]["rsi_mean"], kpis["rsi"]["rsi_std"])
    trend_z = z_score(kpis["trend"]["trend_val"], kpis["trend"]["trend_mean"], kpis["trend"]["trend_std"])
    vol_z = z_score(kpis["vol"]["vol_val"], kpis["vol"]["vol_mean"], kpis["vol"]["vol_std"])
    sentiment_z = z_score(kpis["sentiment"]["sentiment_val"], kpis["sentiment"]["sentiment_mean"], kpis["sentiment"]["sentiment_std"])
    crossover_z = z_score(kpis["crossover"]["crossover_val"], kpis["crossover"]["crossover_mean"], kpis["crossover"]["crossover_std"])

    return {
        "rsi_z": rsi_z,
        "trend_z": trend_z,
        "val_z": vol_z,
        "sentiment_z": sentiment_z,
        "crossover_z": crossover_z,
    }
