class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"This book is {self.title}, and was authored by {self.author}. It has {self.pages} pages. Enjoy your read."
    
    def __repr__(self):
        return f"Book('{self.title}', {self.author}, {self.pages})"
    
book = Book("Kidagaa Kimemwozea", "Ken Walibora", 180)
print(book)
