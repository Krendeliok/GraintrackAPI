from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reserved_goods = relationship('Good', secondary='reserved_goods', back_populates='user_reservations')

    good_associations = relationship('ReservedGood', back_populates='user', viewonly=True)

    def __repr__(self):
        return f'<User {self.name}>'
