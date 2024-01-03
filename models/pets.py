from pydantic import BaseModel, Field, field_validator


class Category(BaseModel):
    id: int = Field(gt=0)
    name: str


class Tag(BaseModel):
    id: int = Field(gt=0)
    name: str


class Pet(BaseModel):
    id: int = Field(gt=0)
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str

    @field_validator("status")
    @classmethod
    def check_status(cls, value):
        valid_statuses = ["available", "pending", "sold"]
        if value in valid_statuses:
            return value
        else:
            raise ValueError("Invalid status")
