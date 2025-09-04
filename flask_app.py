#JUSTIN ISARAPHANICH 9/3/2025 LAST MODIFIED
#FLASK APP FILE, CREATE THE FLASK APP AND THE ROUTES

from flask import Flask, jsonify, request
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

@app.route('/add', methods=['POST'])
def add_data():
    data = Data(title=request.json['title'], satellite=request.json['satellite'])
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Data added successfully'})

@app.route('/<int:id>/delete', methods=['DELETE'])
def delete_date(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data entry deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

# TEST for Flask