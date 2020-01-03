from book.models import Book
import time

def create_test():
    start = time.time()
    for i in range(10000):
        Book.objects.create()
    process_time = time.time() - start
    print(process_time)

def bulk_create_test():
    start = time.time()
    book_objects = []
    for i in range(10000):
        book_objects.append(Book())
    Book.objects.bulk_create(book_objects)
    process_time = time.time() - start
    print(process_time)

