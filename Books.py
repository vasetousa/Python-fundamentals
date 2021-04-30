def add_book(item):
    if item not in books:
        books.insert(0, item)
    return


def take_book(item):
    if item in books:
        books.remove(item)
    return


def swap_books(item1, item2):
    if item1 in books and item2 in books:
        in1 = books.index(item1)
        in2 = books.index(item2)
        books[in1], books[in2] = books[in2], books[in1]
    return


def insert_book(item):
    books.append(item)
    return


def check_book(index):
    if index in range(len(books)):
        print(books[index])
    return


books = input().split("&")
command = input()

while command != "Done":
    order = command.split(" | ")
    book = order[1]
    if order[0] == "Add Book":
        add_book(book)

    elif order[0] == "Take Book":
        take_book(book)

    elif order[0] == "Swap Books":
        book2 = order[2]
        swap_books(book, book2)

    elif order[0] == "Insert Book":
        insert_book(book)

    elif order[0] == "Check Book":
        check_book(book)

    command = input()

print(', '.join(books))