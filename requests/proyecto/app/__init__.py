from flask import Flask
from .countries.routes import countriesBP
from .cities.routes import citiesBP

app = Flask(__name__)

# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(countriesBP, url_prefix='/countries')
app.register_blueprint(citiesBP, url_prefix='/cities')

