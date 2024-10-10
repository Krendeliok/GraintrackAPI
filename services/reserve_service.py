from sqlalchemy import exists
from sqlalchemy.orm import Session

from models import ReservedGood, User

from schemas import Promotion as PromotionSchema, ReservedGood as ReservedGoodSchema
from services.goods_service import decrease_good_quantity, increase_good_quantity


def user_exists(db: Session, user_id: int):
    return db.query(exists().where(User.id == user_id)).scalar()


def reservation_exists(db: Session, reservation_id: int):
    return db.query(exists().where(ReservedGood.id == reservation_id)).scalar()


def create_reservation(db: Session, reserved_good_body: ReservedGoodSchema):
    reserved_good = ReservedGood(**reserved_good_body.model_dump())
    db.add(reserved_good)
    decrease_good_quantity(db, reserved_good.good_id, 1, commit=False)
    db.commit()
    return reserved_good


def delete_reservation(db: Session, reservation_id: int):
    reservation = db.query(ReservedGood).get(reservation_id)
    increase_good_quantity(db, reservation.good_id, 1, commit=False)
    db.delete(reservation)
    db.commit()
    return reservation