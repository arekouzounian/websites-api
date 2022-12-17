from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/test')
def test():
    test = {"key": "value", "test": 1}
    return jsonify(test)

@app.route('/api/v1/interests', methods=['GET'])
def interests():
    interests = []
    with open('./data/interests.txt') as f:
        for line in f.readlines():
            interests.append(line)
    return jsonify(interests), 200

@app.route('/api/v1/about', methods=['GET'])
def about(): 
    about = []
    with open('./data/about.txt') as f: 
        curr = ''
        for line in f.readlines():
            if line == '\n':
                if len(curr) > 1: 
                    about.append(curr)
                    curr = ''
            else: 
                curr += line
    return jsonify(about) 

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, ssl_context=('/etc/letsencrypt/live/api.arekouzounian.com/cert.pem', '/etc/letsencrypt/live/api.arekouzounian.com/privkey.pem'))
