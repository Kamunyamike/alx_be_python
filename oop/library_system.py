class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
    def get_info(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size
    def get_info(self):
        return f"E-Book: {super().get_info()} | File Size: {self.file_size}MB"
class PrintBook (Book):
    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
    def get_info(self):
        return f"Print Book: {super().get_info()} | Pages: {self.page_count}"
    
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book:Book):
        self.books.append(book)

    def list_books(self):
        print("Books in the library")
        for book in self.books:
            print(book.get_info())