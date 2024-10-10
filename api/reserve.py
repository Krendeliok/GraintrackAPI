from fastapi import Depends, HTTPException

from schemas import ReservedGood as ReservedGoodSchema
from sqlalchemy.orm import Session

from api import get_db


from services.goods_service import good_exists, check_good_quantity_mt
from services.reserve_service import user_exists, create_reservation, reservation_exists, delete_reservation


async def reserve_good(reserved_good_body: ReservedGoodSchema, db: Session = Depends(get_db)):
    if not user_exists(db, reserved_good_body.user_id):
        raise HTTPException(status_code=404, detail=f"User with id '{reserved_good_body.user_id}' not found")
    if not good_exists(db, reserved_good_body.good_id):
        raise HTTPException(status_code=404, detail=f"Good with id '{reserved_good_body.good_id}' not found")
    if not check_good_quantity_mt(db, reserved_good_body.good_id, 0):
        raise HTTPException(status_code=400, detail=f"Good with id '{reserved_good_body.good_id}' is out of stock")
    reserved_good = create_reservation(db, reserved_good_body)
    return reserved_good.as_dict()


async def unreserve_good(reservation_id: int, db: Session = Depends(get_db)):
    if not reservation_exists(db, reservation_id):
        raise HTTPException(status_code=404, detail=f"Reservation with id '{reservation_id}' not found")
    deleted_reservation = delete_reservation(db, reservation_id)
    return deleted_reservation.as_dict()
