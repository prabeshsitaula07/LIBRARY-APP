class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        availability = "Available" if self.available else "Not available"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailability: {availability}"

def book_not_found():
    print("Book not found in Library.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' by {book.author} removed from the library.")
        else:
            print("Book not found in the library.")

    def search_by_author(self, author):
        result = []
        for book in self.books:
            if book.author.lower() == author.lower():
                result.append(book)
        return result

    def search_by_title(self, title):
        result = []
        for book in self.books:
            if book.title.lower() == title.lower():
                result.append(book)
        return result

    def search(self, query):
        query = query.lower()
        results = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results

    def search_by_isbn(self, isbn):
        result = []
        for book in self.books:
            if book.isbn == isbn:
                result.append(book)
        return result


    def search_by_title(self, title):
        result = []
        for book in self.books:
            if book.title.lower() == title.lower():
                result.append(book)
        return result

    def search(self, query):
        query = query.lower()
        results = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results


def main():
    library = Library()
    available_choice = ['1','2','3','4','5']
    while True:

        print("\n<----Library Management System ---->")
        print("1. Add Book\n2. Remove Book\n3. Search By Author\n4. Search by Title\n5. Exit\n")
        choice = input("Enter your choice (1-5): ")

        if choice in available_choice:
            if choice == "1":
                title = input("Title of book: ")
                author = input("Author of book: ")
                isbn = input("ISBN: ")
                book = Book(title, author, isbn)
                library.add_book(book)
            
            elif choice == "2":
                title = input("Title of book: ")
                author = input("Author of book: ")
                books = library.search_by_title(title)
                matching_book = [b for b in books if b.author == author]
                if matching_book:
                    if len(matching_book) == 1:
                        library.remove_book(matching_book[0])
                    
                    else:
                        print("Multiple books found.")
                        isbn = input("Enter ISBN of book: ")
                        for book in matching_book:
                            if book.isbn == isbn:
                                library.remove_book(book)
                                break
                            else:
                                book_not_found()
                
                else:
                    book_not_found()

            elif choice == "3":
                author = input("Author of book: ")
                books = library.search_by_author(author)
                if books:
                    print(f"Book by {author}:-\n")
                    for book in books:
                        print(book)
                else:
                    book_not_found()        

            elif choice == "4":
                title = input("Title of book: ")
                books = library.search_by_title(title)
                if books:
                    print(f"Book of title {title}")
                    for book in books:
                        print(book)
                else:
                    book_not_found()

            else:
                print("Exiting the program!! Thank you.")
                break


        else:
            print("Invalid choice!! Choose another.")


if __name__ == "__main__":
    main()