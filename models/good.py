from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from models import Base


class Good(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    promotions = relationship('Promotion', backref='good')
    categories = relationship('Category', secondary="good_categories", back_populates='goods')
    user_reservations = relationship('User', secondary="reserved_goods", back_populates='reserved_goods')

    category_associations = relationship('GoodCategory', back_populates='good', viewonly=True)
    user_associations = relationship('ReservedGood', back_populates='good', viewonly=True)

    def __repr__(self):
        return f'<Good {self.title}>'
