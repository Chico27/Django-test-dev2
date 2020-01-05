from book.models import Book
import time

def len_test():
    bookAll = Book.objects.all()
    start = time.time()
    sum = len(bookAll)
    process_time = time.time() - start
    print(process_time)
    print('sum:' + str(sum))

def count_test():
    bookAll = Book.objects.all()
    start = time.time()
    sum = bookAll.count()
    process_time = time.time() - start
    print(process_time)
    print('sum:' + str(sum))
