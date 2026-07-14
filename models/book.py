from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from models.category import Category


class Book(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    title: str = Field(
        index=True,
        min_length=1,
        max_length=200
    )

    author: str = Field(
        index=True,
        min_length=1,
        max_length=100
    )

    isbn: str = Field(
        unique=True,
        index=True
    )

    published_year: int

    available: bool = Field(
        default=True
    )

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    # Category relationship
    category_id: Optional[int] = Field(
        default=None,
        foreign_key="category.id"
    )

    category: Optional[Category] = Relationship(
        back_populates="books"
    )


class BookCreate(SQLModel):
    title: str
    author: str
    isbn: str
    published_year: int
    category_id: Optional[int] = None


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    available: Optional[bool] = None
    category_id: Optional[int] = None