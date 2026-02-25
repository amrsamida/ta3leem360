from fastapi import APIRouter, HTTPException
from typing import List

from app.models.center import Center, CenterCreate

router = APIRouter(prefix="/centers", tags=["Centers"])

# =====================================================
# In-memory data (temporary – will be replaced by DB)
# =====================================================
centers: List[Center] = [
    Center(id=1, name="Future Academy", city="Suez"),
    Center(id=2, name="Smart Center", city="Cairo"),
]

# =====================================================
# Helpers
# =====================================================
CITY_ALIASES = {
    "cairo": ["cairo", "القاهرة"],
    "suez": ["suez", "السويس"],
}

def normalize_city(city: str) -> str | None:
    city = city.strip().lower()
    for canonical, aliases in CITY_ALIASES.items():
        if city in (alias.lower() for alias in aliases):
            return canonical
    return None


# =====================================================
# LIST + FILTER + SEARCH + PAGINATION
# =====================================================
@router.get("/", response_model=List[Center])
def list_centers(
    city: str | None = None,
    q: str | None = None,
    limit: int = 10,
    offset: int = 0,
):
    results = centers

    if city:
        normalized = normalize_city(city)
        if not normalized:
            return []
        results = [c for c in results if c.city.lower() == normalized]

    if q:
        q = q.lower()
        results = [c for c in results if q in c.name.lower()]

    return results[offset : offset + limit]


# =====================================================
# CREATE
# =====================================================
@router.post("/", response_model=Center, status_code=201)
def create_center(data: CenterCreate):
    new_id = max((c.id for c in centers), default=0) + 1

    new_center = Center(
        id=new_id,
        name=data.name,
        city=data.city,
    )

    centers.append(new_center)
    return new_center


# =====================================================
# GET BY ID
# =====================================================
@router.get("/{center_id}", response_model=Center)
def get_center(center_id: int):
    for center in centers:
        if center.id == center_id:
            return center
    raise HTTPException(status_code=404, detail="Center not found")


# =====================================================
# DELETE
# =====================================================
@router.delete("/{center_id}")
def delete_center(center_id: int):
    for index, center in enumerate(centers):
        if center.id == center_id:
            centers.pop(index)
            return {"message": "Center deleted successfully"}

    raise HTTPException(status_code=404, detail="Center not found")