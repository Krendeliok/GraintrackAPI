from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reserved_goods = relationship(secondary='reserved_goods', back_populates='user')

    good_associations = relationship(back_populates='user')

    def __repr__(self):
        return f'<User {self.name}>'
