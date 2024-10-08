from sqlalchemy import Column, Integer, Float, ForeignKey

from models import Base


class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, ForeignKey('goods.id'))
    discount = Column(Float)

    def __repr__(self):
        return f'<Promotion {self.id} {self.good.title}>'
