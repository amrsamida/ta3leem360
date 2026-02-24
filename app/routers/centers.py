from fastapi import APIRouter

router = APIRouter(prefix="/centers", tags=["Centers"])

centers = [
    {"id": 1, "name": "Future Academy", "city": "Suez"},
    {"id": 2, "name": "Smart Center", "city": "Cairo"},
]

@router.get("/")
def list_centers(city: str | None = None):
    if city:
        return [
            c for c in centers
            if c["city"].lower() == city.lower()
        ]
    return centers
if city:
        results = [
            c for c in results
            if c["city"].lower() == city.lower()
        ]

    if q:
        results = [
            c for c in results
            if q.lower() in c["name"].lower()
        ]

    return results