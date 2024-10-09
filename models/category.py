from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, nullable=True)

    goods = relationship('Good', secondary="good_categories", back_populates='categories')

    good_associations = relationship('GoodCategory', back_populates='category', viewonly=True)

    def __repr__(self):
        return f'<Category {self.name}>'