from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import SessionLocal
from app.models.db_center import Center as DBCenter
from app.models.center import Center, CenterCreate, CenterUpdate

router = APIRouter(prefix="/centers", tags=["Centers"])


# Dependency للحصول على Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# GET /centers
# =========================
@router.get("/", response_model=List[Center])
def list_centers(
    city: Optional[str] = None,
    q: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(DBCenter)

    if city:
        query = query.filter(DBCenter.city == city)

    if q:
        query = query.filter(DBCenter.name.contains(q))

    centers = query.offset(skip).limit(limit).all()
    return centers


# =========================
# GET /centers/{id}
# =========================
@router.get("/{center_id}", response_model=Center)
def get_center(center_id: int, db: Session = Depends(get_db)):
    center = db.query(DBCenter).filter(DBCenter.id == center_id).first()

    if not center:
        raise HTTPException(status_code=404, detail="Center not found")

    return center


# =========================
# POST /centers
# =========================
@router.post("/", response_model=Center)
def create_center(center: CenterCreate, db: Session = Depends(get_db)):
    db_center = DBCenter(
        name=center.name,
        city=center.city,
        description=center.description,
    )

    db.add(db_center)
    db.commit()
    db.refresh(db_center)

    return db_center


# =========================
# DELETE /centers/{id}
# =========================
@router.delete("/{center_id}")
def delete_center(center_id: int, db: Session = Depends(get_db)):
    center = db.query(DBCenter).filter(DBCenter.id == center_id).first()

    if not center:
        raise HTTPException(status_code=404, detail="Center not found")

    db.delete(center)
    db.commit()

    return {"message": "Center deleted successfully"}