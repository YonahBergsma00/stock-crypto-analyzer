import numpy as np

def z_score(value, mean, std):
    return (value - mean) / std if std > 0 else 0

def probability_up(rsi_z, trend_z, vol_z, w=(0.4,0.4,0.2), b=0.05):
    """
    Returns probability that the asset will go up (0-1) based on z-scores
    """
    linear_combination = w[0]*rsi_z + w[1]*trend_z + w[2]*vol_z + b
    prob = 1 /(1 + np.exp(-linear_combination))
    return prob


def z_score_regressors(rsi_val, trend_val, vol_val,
                   rsi_mean, rsi_std, trend_mean, trend_std, vol_mean, 
                   vol_std) -> dict:
    """
    Combine z-scores of RSI, trend, and volatility into a final score.
    weights = importance of each KPI
    Returns a value that can be interpreted as "buy strength"
    """
    rsi_z = z_score(rsi_val, rsi_mean, rsi_std)
    trend_z = z_score(trend_val, trend_mean, trend_std)
    vol_z = z_score(vol_val, vol_mean, vol_std)

    return {
        "rsi_z": rsi_z,
        "trend_z": trend_z,
        "val_z": vol_z,
    }

def convert_score(score: float) -> str:
    
    if score > 0.5:
        return "Buy"
    elif (score >= -0.5) and (score <= 0.5):
        return "Hold"
    else:
        return "Avoid"