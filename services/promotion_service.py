from sqlalchemy.orm import Session

from models import Promotion

from schemas import Promotion as PromotionSchema


def create_promotion(db: Session, promotion: PromotionSchema):
    promotion = Promotion(**promotion.model_dump())
    db.add(promotion)
    db.commit()
    return promotion