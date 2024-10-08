from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, nullable=True)

    goods = relationship(secondary="good_categories", back_populates='category')

    good_associations = relationship(back_populates='category')

    def __repr__(self):
        return f'<Category {self.name}>'