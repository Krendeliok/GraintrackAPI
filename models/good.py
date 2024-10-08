from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from models import Base


class Good(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    promotions = relationship('Promotion', back_populates='good')
    categories = relationship(secondary="good_categories", back_populates='goods')
    user_reservations = relationship(secondary='reserved_goods', back_populates='goods')

    category_association = relationship(back_populates='good')
    user_association = relationship(back_populates='good')

    def __repr__(self):
        return f'<Good {self.title}>'
