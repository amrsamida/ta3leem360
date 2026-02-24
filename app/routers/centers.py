from fastapi import APIRouter

router = APIRouter(prefix="/centers", tags=["Centers"])

@router.get("/")
def list_centers():
    return [
        {"id": 1, "name": "Future Academy", "city": "Suez"},
        {"id": 2, "name": "Smart Center", "city": "Cairo"}
    ]