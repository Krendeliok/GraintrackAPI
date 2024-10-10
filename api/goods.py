from fastapi import Depends, HTTPException, Query
from typing import Annotated

from sqlalchemy.orm import Session

from schemas import (
    Good as GoodSchema,
    Filter, UpdateGood
)
from api import get_db

from services.goods_service import (
    get_goods_by_filter,
    good_exists,
    categories_exist,
    delete_good as delete_good_,
    update_good as update_good_,
    create_good as create_good_,
    sell_good as sell_good_
)


async def get_goods(filters: Annotated[Filter, Query()], db: Session = Depends(get_db)):
    if filters.categories and not categories_exist(db, filters.categories):
        raise HTTPException(status_code=404, detail=f"One of categories not found")
    goods = get_goods_by_filter(db, filters)
    return [good.as_dict() for good in goods]


async def delete_good(good_id: int, db: Session = Depends(get_db)):
    if not good_exists(db, good_id):
        raise HTTPException(status_code=404, detail=f"Good with id '{good_id}' not found")
    deleted_good = delete_good_(db, good_id)
    return deleted_good.as_dict()


async def update_good(good_id: int, good_body: UpdateGood, db: Session = Depends(get_db)):
    if not good_exists(db, good_id):
        raise HTTPException(status_code=404, detail=f"Good with id '{good_id}' not found")
    updated_good = update_good_(db, good_id, good_body)
    return updated_good.as_dict()


async def create_good(good: GoodSchema, db: Session = Depends(get_db)):
    if not categories_exist(db, [good.category_id]):
        raise HTTPException(status_code=404, detail=f"Category with id '{good.category_id}' not found")
    created_good = create_good_(db, good)
    return created_good.as_dict()


async def sell_good(good_id: int, db: Session = Depends(get_db)):
    if not good_exists(db, good_id):
        raise HTTPException(status_code=404, detail=f"Good with id '{good_id}' not found")
    sold_good = sell_good_(db, good_id)
    return sold_good.as_dict()
