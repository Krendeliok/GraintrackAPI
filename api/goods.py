from fastapi import Depends, HTTPException, Query
from typing import Annotated
from sqlalchemy.orm import Session

from models import Good
from schemas import (
    Good as GoodSchema,
    Filter
)
from api import get_db


async def get_goods(filters: Annotated[Filter, Query()], db: Session = Depends(get_db)):
    goods = db.query(Good).all()
    return [good.as_dict() for good in goods]


async def delete_good(good_id: int, db: Session = Depends(get_db)):
    good = db.query(Good).get(good_id)
    if not good:
        raise HTTPException(status_code=404, detail=f"Good with id '{good_id}' not found")
    db.delete(good)
    db.commit()
    return good.as_dict()


async def update_good(good_id: int, good_body: GoodSchema, db: Session = Depends(get_db)):
    good = db.query(Good).get(good_id)
    if not good:
        raise HTTPException(status_code=404, detail=f"Good with id '{good_id}' not found")
    good.__dict__.update(good_body.model_dump(exclude_unset=True))
    db.commit()
    return good.first().as_dict()


async def create_good(good: GoodSchema, db: Session = Depends(get_db)):
    good = Good(**good.model_dump())
    db.add(good)
    db.commit()
    return good.as_dict()


async def sell_good(good_id: int, db: Session = Depends(get_db)):
    good = db.query(Good).get(good_id)
    if not good:
        raise HTTPException(status_code=404, detail=f"Good with id '{good_id}' not found")
    good.quantity -= 1
    db.commit()
    return good.as_dict()
