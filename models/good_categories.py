from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from models import Base


class GoodCategory(Base):
    __tablename__ = 'good_categories'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer)
    category_id = Column(Integer)

    good = relationship(back_populates='category_associations')
    category = relationship(back_populates='good_associations')

    def __repr__(self):
        return f'<GoodCategory {self.id} {self.good.title} {self.category.name}>'