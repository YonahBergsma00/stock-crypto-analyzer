from fastapi import FastAPI
from app.api.analyze import router as analyze_router

app = FastAPI(title="Stocks & Crypto Analyzer")

app.include_router(analyze_router)