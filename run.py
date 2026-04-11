from flask import Flask, render_template, request, jsonify, session
import app as juego

application = Flask(__name__)

application.secret_key = 'sup3rs3cr3t0.2850!'

# Ruta para iniciar un nuevo juego
@application.route('/', methods = ['GET'])
# Ruta para manejar las adivinanzas del usuario
def inicio():

   session['estado'] = juego.crear_juego() # Crear un nuevo juego y almacenar el estado en la sesión

   return  render_template('/index.html') # Renderizar la plantilla HTML para el juego





if __name__ == "__main__":
	application.run(debug=True)
