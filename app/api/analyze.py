from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze")
def analyze(ticker:str):
    return{
        "ticker":ticker,
        "status": "KPI engine coming online"
    }