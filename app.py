#paqueterías externas ---------------------------------------------
from flask import Flask, render_template, redirect, url_for

#inicializar la aplicación ---------------------------------------
app = Flask(__name__)

#rutas ------------------------------------------------------------

#ruta principal
@app.route('/')
def index():
    return render_template('index.html')

#ruta de prueba
@app.route('/login')
def login():
    return 'Login'

@app.route('/definir_tasas')
def definir_tasas():
    return render_template('tasas.html')

#correrr la aplicación -------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)