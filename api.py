```python
from flask import Flask, jsonify, request
app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if 'title' not in new_book or 'author' not in new_book:
        return jsonify({"error": "Invalid data"}), 400
    
    books.append({
        "id": len(books) + 1,
        "title": new_book['title'],
        "author": new_book['author']
    })
    return jsonify(new_book), 201

@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    data = request.get_json()
    if 'title' in data:
        book['title'] = data['title']
    if 'author' in data:
        book['author'] = data['author']
    
    return jsonify(book)

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    books.remove(book)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```