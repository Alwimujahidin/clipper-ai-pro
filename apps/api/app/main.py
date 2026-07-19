from fastapi import FastAPI

app = FastAPI(
    title="Clipper AI Pro API",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "Clipper AI Pro API"
    }

@app.get("/health")
async def health():
    return {
        "healthy": True
    }
