from pydantic import BaseModel


class User(BaseModel):
    name: str


class Good(BaseModel):
    title: str
    price: float
    quantity: int


class Category(BaseModel):
    name: str
    category_id: int


class Promotion(BaseModel):
    good_id: int
    discount: float


class ReservedGood(BaseModel):
    good_id: int
    user_id: int
