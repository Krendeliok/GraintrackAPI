from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class ReservedGood(Base):
    __tablename__ = 'reserved_goods'

    id = Column(Integer, primary_key=True)
    good_id = Column(Integer, ForeignKey('goods.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    good = relationship('Good', back_populates='user_associations', viewonly=True)
    user = relationship('User', back_populates='good_associations', viewonly=True)

    def __repr__(self):
        return f'<ReservedGood {self.id} {self.good.title} {self.user.name}>'