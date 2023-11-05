from fastapi import FastAPI
app = FastAPI()




# یک فهرست ساده برای نگهداری کتاب‌ها
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

# مسیر برای دریافت تمام کتاب‌ها
@app.get("/books")
def get_books():
    return books

# مسیر برای دریافت یک کتاب با شناسه مشخص
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "کتاب مورد نظر یافت نشد"}

# مسیر برای افزودن کتاب جدید
@app.post("/books")
def add_book(book: dict):
    new_book_id = len(books) + 1
    book["id"] = new_book_id
    books.append(book)
    return book

# مسیر برای ویرایش کتاب با شناسه مشخص
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for book in books:
        if book["id"] == book_id:
            book.update(updated_book)
            return {"message": "کتاب به‌روزرسانی شد"}
    return {"error": "کتاب مورد نظر یافت نشد"}

# مسیر برای حذف کتاب با شناسه مشخص
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "کتاب حذف شد"}
    return {"error": "کتاب مورد نظر یافت نشد"}