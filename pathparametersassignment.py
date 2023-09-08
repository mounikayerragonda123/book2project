"""
Here is your opportunity to keep learning!
1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
"""
from fastapi import Body,FastAPI

app=FastAPI()

Books=[
    {"title":"title one","author":"author one","category":"math"},
{"title":"title two","author":"author two","category":"math"},
{"title":"title three","author":"author three","category":"science"},
{"title":"title four","author":"author four","category":"history"},
{"title":"title five","author":"author two","category":"math"}
]

@app.get("/books/{book_author}")
async def read_all_books(book_author: str):
    books_to_return=[]
    for book in Books:
        if book.get('author').casefold()==book_author.casefold():
            books_to_return.append(book)

    return books_to_return