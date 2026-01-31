
from fastapi import FastAPI

app = FastAPI(title="Stock & Crypto Analyzer")

@app.get("/")
def read_root():
    return {"message": "Hello, Analyzer!"}
