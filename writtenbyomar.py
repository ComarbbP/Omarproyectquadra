from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/quadra"
mongo = PyMongo(app)

@app.route('/api/places', methods=['GET'])
def get_places():
    places = mongo.db.places.find()
    return dumps(places), 200

@app.route('/api/places', methods=['POST'])
def add_place():
    data = request.json
    mongo.db.places.insert_one(data)
    return jsonify({'message': 'Place added successfully'}), 201

@app.route('/api/places/<place_id>/rating', methods=['POST'])
def add_rating(place_id):
    data = request.json
    mongo.db.places.update_one({'_id': place_id}, {'$push': {'ratings': data}})
    return jsonify({'message': 'Rating added successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
