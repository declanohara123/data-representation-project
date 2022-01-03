from flask import Flask, json, url_for, request, redirect, abort, jsonify
from FilmsDao import filmsDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"
#get all

@app.route('/films')
def getAll():
    return jsonify(filmsDao.getAll())
#find by id

@app.route('/films/<int:ISBN>')
def findById(ISBN):
    return jsonify(filmsDao.findById(ISBN))

@app.route('/films', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    film = {
        "ISBN": request.json["ISBN"], 
        "title": request.json["title"],
        "director": request.json["director"],
        "year": request.json["year"]
    }
    return jsonify(filmsDao.create(film))

    return "served by Create"


@app.route('/films/<int:ISBN>', methods=['PUT'])
def update(ISBN):
    foundFilms = filmsDao.findById(ISBN)
    if foundFilms == 0:
        return jsonify({}), 404
    currentFilms = foundFilms
    if 'title' in request.json:
            currentFilms['title'] = request.json['title']
    if 'director' in request.json:
            currentFilms['director'] = request.json['director']
    if 'year' in request.json:
            currentFilms['year'] = request.json['year']
    filmsDao.update(currentFilms)

    return jsonify(currentFilms)


@app.route('/films/<int:ISBN>', methods=['DELETE'])
def delete(ISBN):
    filmsDao.delete(ISBN)
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)

