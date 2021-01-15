from flask import Flask, request ,jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def home() :
    return "Liveness Detection"

@app.route('/test', methods=['POST'])
def livenessdetection():
    data = request.get_json()
    print(data['data'].get('images'))
    return jsonify({'result':True, 'score':60 })

if __name__ == '__main__':
    app.run(debug=True)