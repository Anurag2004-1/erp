from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

students = [
    {"id": 1, "name": "John Doe", "age": 20, "course": "Computer Science"},
    {"id": 2, "name": "Jane Smith", "age": 22, "course": "Mechanical Engineering"},
    {"id": 3, "name": "Alice Johnson", "age": 21, "course": "Electrical Engineering"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
