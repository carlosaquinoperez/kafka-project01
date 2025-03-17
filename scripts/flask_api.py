from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conexión Mongo
client = MongoClient("mongodb://mongodb:27017/")
db = client["transport_db"]
collection = db["trains_flink_clean"]

@app.route('/trains', methods=['GET'])
def get_trains():
    trains = list(collection.find({}, {'_id': 0}))  # excluir _id para no exponerlo
    return jsonify(trains)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
