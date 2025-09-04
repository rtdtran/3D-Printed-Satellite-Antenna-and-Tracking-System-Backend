from flask import Flask, jsonify
from config import Config
from database import db, init_db
from models import Data, Positions

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

@app.route('/')
def hello_world():
    return 'Testing!'

@app.route('/<int:id>', methods=['GET'])
def get_data(id):
    data = Data.query.get(id)
    if data:
        return jsonify({
            'id': data.id,
            'title': data.title,
            'satellite': data.satellite
        })
    return jsonify({'Error': 'Data not found'})

if __name__ == '__main__':
    app.run(debug=True)

# TEST for Flask