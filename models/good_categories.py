from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class GoodCategory(Base):
    __tablename__ = 'good_categories'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, ForeignKey('goods.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    good = relationship('Good', back_populates='category_associations', viewonly=True)
    category = relationship('Category', back_populates='good_associations', viewonly=True)

    def __repr__(self):
        return f'<GoodCategory {self.id} {self.good.title} {self.category.name}>'