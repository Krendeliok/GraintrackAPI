from pydantic import BaseModel, Field


class Filter(BaseModel):
    categories: list[int] | None = None
    limit: int = Field(ge=1, default=10)
    page: int = Field(ge=1, default=1)

    @property
    def offset(self):
        return (self.page - 1) * self.limit


class User(BaseModel):
    name: str


class Good(BaseModel):
    title: str | None
    price: float | None
    quantity: int | None = Field(ge=0)
    category_id: int | None


class UpdateGood(Good):
    title: str = None
    price: float = None
    quantity: int = Field(ge=0, default=None)
    category_id: int = None


class Category(BaseModel):
    name: str
    category_id: int


class Promotion(BaseModel):
    good_id: int
    discount: float = Field(ge=0, le=100)


class ReservedGood(BaseModel):
    good_id: int
    user_id: int
