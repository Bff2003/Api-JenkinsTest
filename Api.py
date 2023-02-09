from flask import *
#from flask import jsonify

app = Flask(__name__)

example_data = [{
    "name": "John",
    "age": 30,
    "city": "New York"
}]  

@app.route('/')
def index():
    return 'search for /api/v1/hello or /api/v1/example'

@app.route('/api/v1/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/example', methods=['GET'])
def get_example():
    return jsonify(example_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)