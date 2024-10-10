from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from models import Good, Category
from schemas import Good as GoodSchema, Filter


def get_good_by_id(db: Session, good_id: int) -> Good:
    return db.query(Good).get(good_id)


def get_goods_by_filter(db: Session, filters: Filter):
    statements = [Good.quantity > 0]
    if filters.categories:
        statements.append(Good.category_id.in_(filters.categories))
    goods = db.query(Good).filter(*statements)
    return goods.offset(filters.offset).limit(filters.limit).all()


def category_exists(db: Session, category_id: int):
    return db.query(exists().where(Category.id == category_id)).scalar()


def categories_exist(db: Session, category_ids: list[int]):
    return all([category_exists(db, category_id) for category_id in category_ids])


def good_exists(db: Session, good_id: int):
    return db.query(exists().where(Good.id == good_id)).scalar()


def check_good_quantity_mt(db: Session, good_id: int, quantity: int):
    return db.query(exists().where(Good.id == good_id).where(Good.quantity > quantity)).scalar()


def decrease_good_quantity(db: Session, good_id: int, quantity: int, commit=True):
    upd_stm = update(Good).where(Good.id == good_id).values(quantity=Good.quantity - quantity)
    db.execute(upd_stm)
    if commit:
        db.commit()


def increase_good_quantity(db: Session, good_id: int, quantity: int, commit=True):
    upd_stm = update(Good).where(Good.id == good_id).values(quantity=Good.quantity + quantity)
    db.execute(upd_stm)
    if commit:
        db.commit()


def delete_good(db: Session, good_id: int):
    good = get_good_by_id(db, good_id)
    db.delete(good)
    db.commit()
    return good


def update_good(db: Session, good_id: int, good_body: GoodSchema):
    upd_stm = update(Good).where(Good.id == good_id).values(good_body.model_dump(exclude_unset=True))
    db.execute(upd_stm)
    db.commit()
    good = get_good_by_id(db, good_id)
    return good


def create_good(db: Session, good_body: GoodSchema):
    good = Good(**good_body.model_dump())
    db.add(good)
    db.commit()
    return good


def sell_good(db: Session, good_id: int):
    decrease_good_quantity(db, good_id, 1)
    good = get_good_by_id(db, good_id)
    return good
