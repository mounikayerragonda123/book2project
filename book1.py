from fastapi import Body,FastAPI

app=FastAPI()

Books=[
    {"title":"title one","author":"author one","category":"math"},
{"title":"title two","author":"author two","category":"math"},
{"title":"title three","author":"author three","category":"science"},
{"title":"title four","author":"author four","category":"history"},
{"title":"title five","author":"author two","category":"math"}
]

@app.get("/books")
async def read_all_books():
    return Books


@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in Books:
        if book.get('title').casefold()==book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in Books:
        if book.get('category').casefold()== category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in Books:
        if book.get('author').casefold()== book_author.casefold() and book.get('category').casefold()== category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
 Books.append(new_book)


@app.put("/books/upadte_book")
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()== updated_book.get('title').casefold():
            Books[i]=updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==book_title.casefold():
            Books.pop(i)
            break