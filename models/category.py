from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    goods = relationship('Good', backref='categories')

    def __repr__(self):
        return f'<Category {self.name}>'
