from typing import Optional

import optional
from fastapi import FastAPI, Path ,Query ,HTTPException
from pydantic import BaseModel, Field
from starlette import status


app=FastAPI()

class Book:
    id: int
    title : str
    author : str
    description : str
    ranking : int

    def __init__(self, id, title, author, description, ranking):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.ranking=ranking



class BookRequest(BaseModel):
    id: int
    title : str =Field(min_length=3)
    author : str =Field(min_length=1)
    description : str =Field(min_lenth=1, max_length=100)
    ranking : int = Field(gt=0,lt=6)

    class config:
        schema_extra={
            'example':{
                'title':'a new book',
                'author':'coding with roby',
                'description':'a new description of a book',
                'rating':'5'
            }
        }

books=[
   Book(1, 'computer science','codybyroby','a very nice book',5),
    Book(2, 'Be with fastapi', 'codybyroby', 'a greatbook', 5),
    Book(3, 'master endpoints', 'codybyroby', 'a awesome book', 5),
    Book(4, 'python', 'codybyroby', 'a good book', 4)

]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return books

@app.get("/books/{book_id}",status_code=status.HTTP_200_OK)
async def read_book(book_id : int =Path(gt=0)):
    for book in books:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_ranking: int =Query(gt=0,lt=6)):
    books_to_return=[]
    for book in books:
        if book.ranking==book_ranking:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.dict())
    books.append(find_book_id(new_book))


def find_book_id(book : Book):
    book.id=1 if len(books)==0 else books[-1].id+1
    return book

@app.put("/books/update_book" , status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book : BookRequest):
    book_changed= False
    for i in range(len(books)):
        if books[i].id==book.id:
            books[i]= book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404 , detail='item not found')

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    book_changed = False
    for i in range(len(books)):
        if books[i].id==book_id:
            books.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404 , detail='item not found')