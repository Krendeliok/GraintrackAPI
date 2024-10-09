from fastapi import Depends, HTTPException

from schemas import ReservedGood as ReservedGoodSchema
from sqlalchemy.orm import Session

from models import ReservedGood, User, Good
from api import get_db


async def reserve_good(reserved_good_body: ReservedGoodSchema, db: Session = Depends(get_db)):
    user = db.query(User).get(reserved_good_body.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id '{reserved_good_body.user_id}' not found")
    good = db.query(Good).get(reserved_good_body.good_id)
    if not good:
        raise HTTPException(status_code=404, detail=f"Good with id '{reserved_good_body.good_id}' not found")
    reserved_good = ReservedGood(**reserved_good_body.model_dump())
    db.add(reserved_good)
    db.commit()
    db.refresh(reserved_good)
    return reserved_good.as_dict()


async def unreserve_good(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(ReservedGood).get(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail=f"Reservation with id '{reservation_id}' not found")
    db.delete(reservation)
    db.commit()
    return reservation.as_dict()
