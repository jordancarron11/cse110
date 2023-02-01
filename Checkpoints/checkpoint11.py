with open("books.txt") as bom_file:
    for line in bom_file:
        book = line.strip()
        print(book)