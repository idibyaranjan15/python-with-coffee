from fastapi import FastAPI
app=FastAPI()
BOOKS = [
    {
        "title": "title one",
        "author": "author one",
        "category": "science"
    },
    {
        "title": "title two",
        "author": "author two",
        "category": "arts"
    },
    {
        "title": "title three",
        "author": "author three",
        "category": "arts"
    },
    {
        "title": "title four",
        "author": "author four",
        "category": "commerce"
    },
    {
        "title": "title five",
        "author": "author five",
        "category": "arts"
    },
    {
        "title": "title six",
        "author": "author six",
        "category": "science"
    },
    {
        "title": "title seven",
        "author": "author seven",
        "category": "science"
    },
    {
        "title": "title eight",
        "author": "author eight",
        "category": "commerce"
    },
    {
        "title": "title nine",
        "author": "author nine",
        "category": "arts"
    }
]




@app.get("/books/mybook")
async def read_all_book():
    return {"message":"This is an important message"}
@app.get("/books/{book_title}")
async def read_all_books(book_title:str):
    for book in BOOKS:
        if book.get("title").casefold()==book_title.casefold():
            return book
    
@app.get("/books/{book_author}/")
async def read_ctaegory_by_query(book_author:str,category:str):
        books_to_return=[]
        for book in BOOKS:
            if book.get("category").casefold()==category.casefold()  and book.get("author").casefold()==book_author.casefold():
                books_to_return.append(book)
        return books_to_return