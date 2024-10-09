from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Good(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

    promotions = relationship('Promotion', backref='good')
    user_reservations = relationship('User', secondary="reserved_goods", back_populates='reserved_goods')

    user_associations = relationship('ReservedGood', back_populates='good', viewonly=True)

    def __repr__(self):
        return f'<Good {self.title}>'
