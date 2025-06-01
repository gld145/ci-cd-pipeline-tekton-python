from flask import Flask
from flask_cors import CORS
from service import config
from service.extensions import talisman

app = Flask(__name__)
CORS(app)
app.config.from_object(config)
talisman.init_app(app, force_https=False)


@app.route("/")
def index():
    """Root route"""
    return {
        "name": "Account REST API Service",
        "version": "1.0"
    }
