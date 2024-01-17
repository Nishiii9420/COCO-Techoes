import random
from datetime import datetime, timedelta
class Book:
    def __init__(self, name, checkout_date, return_date):
        self.name= name
        self.checkout_date= checkout_date
        self.return_date= return_date

class Member:
    def __init__(self, name, books=[]):
        self.name = name
        self.books = books

def generate_random_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(1, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)

def generate_library_data(num_members=10, min_books=10, max_books=30):
    library_members = []


    for i in range(1, num_members + 1):
        member_name = f"Member{i}"
        num_books = random.randint(min_books, max_books)

        books = []
        for j in range(1, num_books + 1):
            book_name = f"Book{j}"
            checkout_date = generate_random_date()
            return_date = generate_random_date()
            books.append(Book(book_name, checkout_date, return_date))
        library_members.append(Member(member_name, books))

    return library_members

def calculate_average_days(library_members):
    total_days = 0
    total_books = 0

    for member in library_members:
        for book in member.books:
            total_days += (book.return_date - book.checkout_date).days
            total_books += 1

    return total_days / total_books

# Generate random library data
library_data = generate_library_data()

# Calculate average number of days each member keeps a book
average_days = calculate_average_days(library_data)

print(f"Average number of days each member of the library keeps a book is: {average_days:.2f}")