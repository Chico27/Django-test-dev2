
from book.models import Book
import time

def count_test():
    bookAll = Book.objects.all()
    print(bookAll)
    start = time.time()
    for i in range(10000):
        if bookAll.count() > 0:
            pass
    process_time = time.time() - start
    print(process_time)


def exists_test():
    bookAll = Book.objects.all()
    print(bookAll)
    start = time.time()
    for i in range(10000):
        if bookAll.exists():
            pass
    process_time = time.time() - start
    print(process_time)
