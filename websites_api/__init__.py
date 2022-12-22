from flask import *
import os 
import json

def create_app():
    app = Flask(__name__)

    path = os.path.dirname(__file__)
    
    @app.route('/api/v1/interests', methods=['GET'])
    def interests():
        interests = []
        with open(path + '/data/interests.txt') as f:
            for line in f.readlines():
                interests.append(line)
        return jsonify(interests), 200

    @app.route('/api/v1/about', methods=['GET'])
    def about(): 
        about = []
        with open(path + '/data/about.txt') as f: 
            curr = ''
            for line in f.readlines():
                if line == '\n':
                    if len(curr) > 1: 
                        about.append(curr)
                        curr = ''
                else: 
                    curr += line
        return jsonify(about) 
    
    @app.route('/api/v1/projects', methods=['GET'])
    def test():
        with open(path + '/data/projects.json', 'r') as f:
            return json.loads(f.read())
    return app
