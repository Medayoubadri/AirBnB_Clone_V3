#!/usr/bin/python3
"""
Flask Application
"""
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, make_response, jsonify
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
swagger = Swagger(app)

app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(error):
    """
    Close Storage
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    404 Error
    returns a JSON-formatted 404 status code response
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
