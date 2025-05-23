from flask import Flask
from service import config  # ✅ Nécessaire pour que la ligne suivante fonctionne
from service.extensions import talisman

app = Flask(__name__)
app.config.from_object(config)

talisman.init_app(app, force_https=False)