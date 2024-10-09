from pydantic import BaseModel


class Filter(BaseModel):
    categories: list[int] | None = None
    limit: int = 10
    page: int = 1


class User(BaseModel):
    name: str


class Good(BaseModel):
    title: str | None = None
    price: float | None = None
    quantity: int | None = None


class Category(BaseModel):
    name: str
    category_id: int


class Promotion(BaseModel):
    good_id: int
    discount: float


class ReservedGood(BaseModel):
    good_id: int
    user_id: int
