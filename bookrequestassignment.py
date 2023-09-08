"""
Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.
Enhance each Book to now have a published_date
Then create a new GET Request method to filter by published_date
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()
class Book:
    id: int
    title : str
    author : str
    description : str
    rating: int
    published_date: int


    def __init__(self, id, title, author, description, rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date


class BookRequest(BaseModel):
    id: int
    title : str =Field(min_length=3)
    author : str =Field(min_length=1)
    description : str =Field(min_lenth=1, max_length=100)
    ranking : int = Field(gt=0,lt=6)
    published_date : int =Field(gt=1999, lt=2031)


books=[
   Book(1, 'computer science','codybyroby','a very nice book',5,2012),
    Book(2, 'Be with fastapi', 'codybyroby', 'a greatbook', 5,2012),
    Book(3, 'master endpoints', 'codybyroby', 'a awesome book', 5,2023),
    Book(4, 'python', 'codybyroby', 'a good book', 4,2022)
]

@app.get("/books/{published_date}")
async def read_books_by_publish_date(published_date :int):
    books_to_return = []
    for book in books:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return
