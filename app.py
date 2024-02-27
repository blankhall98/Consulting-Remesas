#paqueterías externas ---------------------------------------------
from flask import Flask

#inicializar la aplicación ---------------------------------------
app = Flask(__name__)

#rutas ------------------------------------------------------------

#ruta principal
@app.route('/')
def index():
    return 'Plataforma'

#ruta de prueba
@app.route('/login')
def login():
    return 'Login'

@app.route('/definir_tasas')
def definir_tasas():
    return 'Registro'

#correrr la aplicación -------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)