
def convert_score(prob: float) -> str:
    
    if prob > 0.85:
        return "Strong Buy"
    elif prob >= 0.7:
        return "Buy"
    elif prob >= 0.55:
        return "Hold"
    elif prob >= 0.45:
        return "Avoid"
    else:
        return "Strong Avoid"