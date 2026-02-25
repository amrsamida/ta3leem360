from fastapi import FastAPI
from app.database import engine, Base
from app.models import db_center
from app.routers.centers import router as centers_router

app = FastAPI()

# 👇 السطر المهم
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(centers_router)