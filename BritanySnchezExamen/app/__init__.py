from flask import Flask
from bandas.routes import bandasBP
from canciones.routes import cancionesBP
from users.routes import usersBP

from flask_jwt_extended import JWTManager

app =Flask(__name__)
app.register_blueprint(bandasBP,url_prefix='/bandas')
app.register_blueprint(cancionesBP, url_prefix='/canciones')
app.register_blueprint(usersBP, url_prefix='/users')

#RUN CODE

if __name__=='__main__':
    app.run(debug=True, hosto='0.0.0.0', port=5050)
    
    
#config de autenticación

app.config['SECRET_KEY']='clave'
jwt =JWTManager(app)
    