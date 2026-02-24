from fastapi import FastAPI
from app.routers.centers import router as centers_router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(centers_router)