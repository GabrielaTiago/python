from flask import request, jsonify
from app import app, sqlite, Author, Post
from default_messages import  AUTORS_NOT_FOUND_MESSAGE, AUTHOR_NOT_FOUND_MESSAGE, AUTHOR_CREATED_MESSAGE, AUTHOR_UPDATED_MESSAGE, AUTHOR_DELETED_MESSAGE, POSTS_NOT_FOUND_MESSAGE, POST_NOT_FOUND_MESSAGE, POST_CREATED_MESSAGE, POST_UPDATED_MESSAGE, POST_DELETED_MESSAGE

def mount_author(author):
    return {
        'id': author.id,
        'name': author.name,
        'email': author.email,
        'password': author.password,
        'admin': author.admin
    }

# Author routes

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = sqlite.get_all(Author)

    if len(authors) == 0:
        return jsonify({'message': AUTORS_NOT_FOUND_MESSAGE}), 404

    list_authors = []
    for author in authors:
        __author = mount_author(author)
        list_authors.append(__author)

    return jsonify({'authors': list_authors, 'total': len(list_authors)})


@app.route('/author/<int:id>', methods=['GET'])
def get_author(id):
    author = sqlite.get(Author, id)

    if not author:
        return jsonify({'message': AUTHOR_NOT_FOUND_MESSAGE}), 404

    __author = mount_author(author)
    return jsonify(__author)

@app.route('/author', methods=['POST'])
def add_author():
    data = request.get_json()

    if not data['name'] or not data['email'] or not data['password'] or not data['admin']:
        return jsonify({'message': 'All fields are required'}), 406

    author = Author(data['name'], data['email'], data['password'], data['admin'])
    sqlite.add(author)
    return jsonify({'message': AUTHOR_CREATED_MESSAGE }), 201

@app.route('/author/<int:id>', methods=['PUT'])
def update_author(id):
    author = sqlite.get(Author, id)

    if not author:
        return jsonify({'message': AUTHOR_NOT_FOUND_MESSAGE}), 404

    data = request.get_json()
    author.name = data['name']
    author.email = data['email']
    author.password = data['password']
    author.admin = data['admin']
    sqlite.update()
    return jsonify({'message': AUTHOR_UPDATED_MESSAGE})

@app.route('/author/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = sqlite.get(Author, id)

    if not author:
        return jsonify({'message': AUTHOR_NOT_FOUND_MESSAGE}), 404

    sqlite.delete(author)
    return jsonify({'message': AUTHOR_DELETED_MESSAGE})

def mount_post(post):
    return {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author_id': post.author_id
    }

# Post routes

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = sqlite.get_all(Post)

    if len(posts) == 0:
        return jsonify({'message': POSTS_NOT_FOUND_MESSAGE}), 404

    list_posts = [mount_post(post) for post in posts]
    return jsonify({'posts': list_posts, 'total': len(list_posts)})

@app.route('/post/<int:id>', methods=['GET'])
def get_post(id):
    post = sqlite.get(Post, id)

    if post is None:
        return jsonify({'message': POST_NOT_FOUND_MESSAGE}), 404

    return jsonify(mount_post(post))

@app.route('/post', methods=['POST'])
def add_post():
    data = request.get_json()

    if not data['title'] or not data['content'] or not data['author_id']:
        return jsonify({'message': 'All fields are required'}), 406

    post = Post(data['title'], data['content'], data['author_id'])
    sqlite.add(post)
    return jsonify({'message': POST_CREATED_MESSAGE}), 201

@app.route('/post/<int:id>', methods=['PUT'])
def update_post(id):
    post = sqlite.get(Post, id)

    if not post:
        return jsonify({'message': POST_NOT_FOUND_MESSAGE}), 404

    data = request.get_json()

    post.title = data['title']
    post.content = data['content']
    post.author_id = data['author_id']
    sqlite.update()
    return jsonify({'message': POST_UPDATED_MESSAGE})

@app.route('/post/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = sqlite.get(Post, id)

    if not post:
        return jsonify({'message': POST_NOT_FOUND_MESSAGE}), 404

    sqlite.delete(post)
    return jsonify({'message': POST_DELETED_MESSAGE})


app.run(port=5000, host='localhost', debug=True)