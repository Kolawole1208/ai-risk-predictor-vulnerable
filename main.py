from fastapi import FastAPI

app = FastAPI(
    title="AI Risk Predictor - Vulnerable (Clean Baseline)",
    description="Minimal clean baseline app for the AI Risk Predictor experiments",
)


@app.get("/")
async def read_root():
    return {"message": "AI Risk Predictor - clean baseline"}


@app.get("/health")
async def health():
    return {"status": "ok"}


# Uvicorn entrypoint for local runs: `uvicorn main:app --reload`
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
