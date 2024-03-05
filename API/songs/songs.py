from flask import Flask, request, jsonify

app = Flask(__name__)

songs = [
    {
        'id': 1,
        'cancao': 'I drink wine',
        'estilo': 'Pop'
    },
    {
        'id': 2,
        'cancao': 'Easy on me',
        'estilo': 'Pop'
    },
    {
        'id': 3,
        'cancao': 'Someone like you',
        'estilo': 'Pop'
    }
]

@app.route('/cancoes', methods=['POST'])
def add_song():
    new_id = len(songs) + 1
    song = request.get_json()
    song['id'] = new_id
    songs.append(song)
    return jsonify(song), 201

@app.route('/cancoes', methods=['GET'])
def get_songs():
    return jsonify(songs)

@app.route('/cancoes/<int:id>', methods=['GET'])
def get_song_by_id(id):
    for song in songs:
        if song['id'] == id:
            return jsonify(song)
    return jsonify({'message': 'Canção não encontrada!'}), 404


@app.route('/cancoes/<int:id>', methods=['PUT'])
def update_song(id):
    song = request.get_json()
    for i in range(len(songs)):
        if songs[i]['id'] == id:
            songs[i] = song
            return jsonify(song)
    return jsonify({'message': 'Canção não encontrada!'}), 404


@app.route('/cancoes/<int:id>', methods=['DELETE'])
def delete_song(id):
    for i in range(len(songs)):
        if songs[i]['id'] == id:
            del songs[i]
            return jsonify({'message': 'Canção deletada com sucesso!'})
    return jsonify({'message': 'Canção não encontrada!'}), 404

app.run(port=5000, host='localhost', debug=True)