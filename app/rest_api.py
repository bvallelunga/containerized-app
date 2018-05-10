"""
We wrap our
"""
from flask import Flask
from flask import request
from flask import jsonify

from main import ModelInterface

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.is_json:
        return jsonify(ModelInterface().prediction(request.get_json()))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
