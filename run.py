from flask import Flask, render_template, request, session, redirect, url_for # type: ignore
import app as juego

app = Flask(__name__)

app.secret_key = 'sup3rs3cr3t0.2850!'

# Ruta para iniciar un nuevo juego
@app.route('/', methods = ['GET'])
# Ruta para manejar las adivinanzas del usuario
def inicio():
	if 'estado' not in session:
		session['estado'] = juego.crear_juego()
	return render_template('index.html')

@app.route('/adivinar', methods = ['GET','POST'])
def adivinar():
	numero = int(request.form['numero'])
	resultado = juego.adivinar(numero, session['estado'])
	return render_template('index.html', resultado=resultado)


if __name__ == "__main__":
	app.run(debug=True)
