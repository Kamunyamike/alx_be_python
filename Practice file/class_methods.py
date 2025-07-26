class Book:
    total_books = 0
    def __init__(self, name):
        self.name = name
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"The total number of books created is {cls.total_books}")

book1 = Book("Machine Learning")
book2 = Book("Learn Django")
book3 = Book("Understanding Python Programming")
book4 = Book("DAX")
book5 = Book("Learn Tableau")
book6 = Book("Think Big")
book7 = Book("Business Intelligence")


Book.display_total_books()