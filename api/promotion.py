from fastapi import Depends, HTTPException

from schemas import Promotion as PromotionSchema
from sqlalchemy.orm import Session

from api import get_db

from services.goods_service import good_exists
from services.promotion_service import create_promotion as create_promotion_


async def create_promotion(promotion: PromotionSchema, db: Session = Depends(get_db)):
    if not good_exists(db, promotion.good_id):
        raise HTTPException(status_code=404, detail=f"Good with id '{promotion.good_id}' not found")
    created_promotion = create_promotion_(db, promotion)
    return created_promotion.as_dict()
