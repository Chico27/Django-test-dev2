from book.models import Book
import time


def create_data():
    # start = time.time()
    book_objects = []
    for i in range(10000):
        book_objects.append(Book(title='title' + str(i+1)))
    Book.objects.bulk_create(book_objects)
    # process_time = time.time() - start
    # print(process_time)


def update_test():
    bookAll = Book.objects.all()
    start = time.time()
    for i, book in enumerate(bookAll):
        book.title = 'changed' + str(i+1)
        book.save()
    process_time = time.time() - start
    print(process_time)


def bulk_update_test():
    bookAll = Book.objects.all()
    start = time.time()
    book_objects = []
    for i, book in enumerate(bookAll):
        book.title = 'changed' + str(i+1)
        book_objects.append(book)
    Book.objects.bulk_update(book_objects, ['title'])
    process_time = time.time() - start
    print(process_time)


