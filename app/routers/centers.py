from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/centers", tags=["Centers"])

centers = [
    {"id": 1, "name": "Future Academy", "city": "Suez"},
    {"id": 2, "name": "Smart Center", "city": "Cairo"},
]

CITY_ALIASES = {
    "cairo": ["cairo", "القاهرة"],
    "suez": ["suez", "السويس"],
}

def normalize_city(city: str) -> str | None:
    city = city.strip().lower()
    for canonical, aliases in CITY_ALIASES.items():
        if city in [a.lower() for a in aliases]:
            return canonical
    return None


# ✅ LIST + FILTER + SEARCH + PAGINATION
@router.get("/")
def list_centers(
    city: str | None = None,
    q: str | None = None,
    limit: int = 10,
    offset: int = 0
):
    results = centers

    if city:
        normalized = normalize_city(city)
        if normalized:
            results = [
                c for c in results
                if c["city"].lower() == normalized
            ]
        else:
            return []

    if q:
        q = q.lower()
        results = [
            c for c in results
            if q in c["name"].lower()
        ]

    return results[offset : offset + limit]


# ✅ GET BY ID
@router.get("/{center_id}")
def get_center(center_id: int):
    for center in centers:
        if center["id"] == center_id:
            return center

    raise HTTPException(status_code=404, detail="Center not found")