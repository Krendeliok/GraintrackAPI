from sqlalchemy.orm import configure_mappers

from models.base import Base

from models.category import Category
from models.good import Good
from models.good_categories import GoodCategory
from models.promotion import Promotion
from models.reserved_goods import ReservedGood
from models.user import User


configure_mappers()
