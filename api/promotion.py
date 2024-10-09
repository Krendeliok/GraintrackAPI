from fastapi import Depends

from schemas import Promotion as PromotionSchema
from sqlalchemy.orm import Session

from models import Promotion
from api import get_db


async def create_promotion(promotion: PromotionSchema, db: Session = Depends(get_db)):
    promotion = Promotion(**promotion.model_dump())
    db.add(promotion)
    db.commit()
    return promotion.as_dict()
