from flask import request, jsonify, make_response
from app import app, sqlite, Author, Post
from default_messages import BAD_REQUEST_MESSAGE, AUTORS_NOT_FOUND_MESSAGE, AUTHOR_NOT_FOUND_MESSAGE, AUTHOR_CREATED_MESSAGE, AUTHOR_UPDATED_MESSAGE, AUTHOR_DELETED_MESSAGE, POSTS_NOT_FOUND_MESSAGE, POST_NOT_FOUND_MESSAGE, POST_CREATED_MESSAGE, POST_UPDATED_MESSAGE, POST_DELETED_MESSAGE
from datetime import datetime, timedelta
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user = sqlite.get(Author, data['public_id'])
        except jwt.DecodeError:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(user, *args, **kwargs)
    return decorated

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify user credentials', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    author = sqlite.get(Author, auth.username)

    if not author:
        return make_response('Could not verify user credentials', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if author.password == auth.password:
        token = jwt.encode({'public_id': author.id, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'message': 'Login successful!', 'token': token})
    else:
        return make_response('Your e-mail or password is incorrect', 401, {'WWW-Authenticate': 'Basic realm="Wrong credentials!"'})

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
@token_required
def get_authors(user):
    try:
        authors = sqlite.get_all(Author)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    if len(authors) == 0:
        return jsonify({'message': AUTORS_NOT_FOUND_MESSAGE}), 404
    list_authors = [mount_author(author) for author in authors]
    return jsonify({'authors': list_authors, 'total': len(list_authors)})

@app.route('/author/<int:id>', methods=['GET'])
@token_required
def get_author(user, id):
    try:
        author = sqlite.get(Author, id)
        if not author:
            return jsonify({'message': AUTHOR_NOT_FOUND_MESSAGE}), 404
        __author = mount_author(author)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify(__author)

@app.route('/author', methods=['POST'])
@token_required
def add_author(user):
    data = request.get_json()
    if not data['name'] or not data['email'] or not data['password'] or not data['admin']:
        return jsonify({'message': 'All fields are required'}), 406
    author = Author(data['name'], data['email'], data['password'], data['admin'])
    try:
        sqlite.add(author)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify({'message': AUTHOR_CREATED_MESSAGE }), 201

@app.route('/author/<int:id>', methods=['PUT'])
@token_required
def update_author(user, id):
    try:
        author = sqlite.get(Author, id)
        if not author:
            return jsonify({'message': AUTHOR_NOT_FOUND_MESSAGE}), 404
        data = request.get_json()
        author.name = data['name']
        author.email = data['email']
        author.password = data['password']
        author.admin = data['admin']
        sqlite.update()
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify({'message': AUTHOR_UPDATED_MESSAGE})

@app.route('/author/<int:id>', methods=['DELETE'])
@token_required
def delete_author(user, id):
    try:
        author = sqlite.get(Author, id)
        if not author:
            return jsonify({'message': AUTHOR_NOT_FOUND_MESSAGE}), 404
        sqlite.delete(author)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400

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
@token_required
def get_posts(user):
    try:
        posts = sqlite.get_all(Post)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    if len(posts) == 0:
        return jsonify({'message': POSTS_NOT_FOUND_MESSAGE}), 404
    list_posts = [mount_post(post) for post in posts]
    return jsonify({'posts': list_posts, 'total': len(list_posts)})

@app.route('/post/<int:id>', methods=['GET'])
@token_required
def get_post(user, id):
    try:
        post = sqlite.get(Post, id)
        if post is None:
            return jsonify({'message': POST_NOT_FOUND_MESSAGE}), 404
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify(mount_post(post))

@app.route('/post', methods=['POST'])
@token_required
def add_post(user):
    data = request.get_json()
    if not data['title'] or not data['content'] or not data['author_id']:
        return jsonify({'message': 'All fields are required'}), 406
    post = Post(data['title'], data['content'], data['author_id'])
    try:
        sqlite.add(post)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify({'message': POST_CREATED_MESSAGE}), 201

@app.route('/post/<int:id>', methods=['PUT'])
@token_required
def update_post(user, id):
    try:
        post = sqlite.get(Post, id)
        if not post:
            return jsonify({'message': POST_NOT_FOUND_MESSAGE}), 404
        data = request.get_json()
        post.title = data['title']
        post.content = data['content']
        post.author_id = data['author_id']
        sqlite.update()
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify({'message': POST_UPDATED_MESSAGE})

@app.route('/post/<int:id>', methods=['DELETE'])
@token_required
def delete_post(user, id):
    try:
        post = sqlite.get(Post, id)
        if not post:
            return jsonify({'message': POST_NOT_FOUND_MESSAGE}), 404
        sqlite.delete(post)
    except Exception as e:
        print(e)
        return jsonify({'message': BAD_REQUEST_MESSAGE}), 400
    return jsonify({'message': POST_DELETED_MESSAGE})


app.run(port=5000, host='localhost', debug=True)