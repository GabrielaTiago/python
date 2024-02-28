from flask import Flask, request, jsonify

app = Flask(__name__)

#DATA
books = [
    {
        'title': 'Clean Code',
        'author': 'Robert C. Martin',
        'pages': 464
    },
    {
        'title': 'The Pragmatic Programmer',
        'author': 'Andrew Hunt and David Thomas',
        'pages': 352
    },
    {
        'title': 'Design Patterns',
        'author': 'Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides',
        'pages': 395
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:index>', methods=['GET'])
def get_book(index):
    return jsonify(books[index-1])

@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return jsonify(book)

@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    book = request.get_json()
    books[index-1].update(book)
    return jsonify(book)

@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    if books[index-1]:
        del books[index-1]
        return jsonify(f'Book at index {index} deleted successfully')
    return jsonify(f'Book not found to be erased at index {index}')

app.run(port=5000, host='localhost', debug=True)