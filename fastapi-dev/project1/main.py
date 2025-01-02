from fastapi import FastAPI
app=FastAPI()

BOOKS = [
    {
        "title": "title One",
        "author": "author One",
        "category": "Science"
    },
    {
        "title": "title Two",
        "author": "author Two",
        "category": "Arts"
    },
    {
        "title": "title Three",
        "author": "author Three",
        "category": "Arts"
    },
    {
        "title": "title Four",
        "author": "author Four",
        "category": "Commerce"
    },
    {
        "title": "title Five",
        "author": "author Five",
        "category": "Arts"
    },
    {
        "title": "title Six",
        "author": "author Six",
        "category": "Science"
    },
    {
        "title": "title Seven",
        "author": "author Seven",
        "category": "Science"
    },
    {
        "title": "title Eight",
        "author": "author Eight",
        "category": "Commerce"
    },
    {
        "title": "title Nine",
        "author": "author Nine",
        "category": "Arts"
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
    
