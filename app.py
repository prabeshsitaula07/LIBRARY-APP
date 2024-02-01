from flask import Flask, render_template, request, redirect, url_for
from library_mgmt import Book, Library

app = Flask(__name__)

library = Library()

@app.route('/')
def index():
    head_title = request.args.get('head_title', 'Library Management System')
    return render_template('index.html', books=library.books, head_title=head_title)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    isbn = request.form['isbn']
    book = Book(title, author, isbn)
    library.add_book(book)
    return redirect(url_for('index'))

@app.route('/remove_book/<isbn>', methods=['GET'])
def remove_book(isbn):
    books = library.search_by_isbn(isbn)
    if books:
        for book in books:
            library.remove_book(book)
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():

    head_title = request.args.get('head_title', 'Searched Books')
    query = request.form.get('query')
    results = library.search(query)
    return render_template('search_results.html', results=results, head_title=head_title)

if __name__ == "__main__":
    app.run(debug=True)
