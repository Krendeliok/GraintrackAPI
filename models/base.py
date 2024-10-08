from sqlalchemy.orm import declarative_base


def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base = declarative_base()
Base.__mapper_args__ = {
    'confirm_deleted_rows': False
}
Base.as_dict = as_dict
