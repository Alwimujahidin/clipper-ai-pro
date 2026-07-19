from fastapi import FastAPI

app = FastAPI(title="Clipper AI Pro API")

@app.get("/")
def root():
    return {"message": "Clipper AI Pro API is running"}
