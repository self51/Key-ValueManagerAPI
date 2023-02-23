from flask import Flask, request, jsonify

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongo', 27017)
db = client['my_database']
collection = db['my_collection']


@app.route('/api/create', methods=['POST'])
def create_key_value():
    data = request.get_json()
    key = data['key']
    value = data['value']
    collection.insert_one({'key': key, 'value': value})
    return jsonify({'message': 'Key-value pair created successfully'})


@app.route('/api/update/<key>', methods=['PUT'])
def update_key_value(key):
    get_collection = collection.find_one({'key': key})
    if get_collection is None:
        return jsonify({'error': 'Key not found'})

    data = request.get_json()
    new_value = data['value']
    collection.update_one({'key': key}, {'$set': {'value': new_value}})
    return jsonify({'message': 'Key-value pair updated successfully.'})


@app.route('/api/get/<key>', methods=['GET'])
def get_key_value(key):
    get_collection = collection.find_one({'key': key})
    if get_collection is None:
        return jsonify({'error': 'Key not found'})

    return jsonify({'key': get_collection['key'], 'value': get_collection['value']})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
