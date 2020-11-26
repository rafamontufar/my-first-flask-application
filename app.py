from flask import Flask 
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/users/<id>', methods=['GET'])
def get_users(id):
	response = {'message': 'success'}
	return jsonify(response)

@app.route('/api/v1/users/', methods=['POST'])
def create_users():
	response = {'message': 'Usuario creado con exito'}
	return jsonify(response)

@app.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
	response = {'message': 'Usuario eliminado con exito'}
	return jsonify(response)

if __name__ == '__main__':
	app.run('0.0.0.0')
