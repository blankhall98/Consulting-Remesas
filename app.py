#paqueterías externas ---------------------------------------------
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#inicializar la aplicación ---------------------------------------
app = Flask(__name__)

#configuración de la base de datos --------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///control_caja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#modelos de la base de datos --------------------------------------

#modelo de la tabla de tasas de cambio
class TasaDeCambio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    tasa_oficial = db.Column(db.Float, nullable=False)
    tasa_compra = db.Column(db.Float, nullable=False)
    tasa_venta = db.Column(db.Float, nullable=False)
    tasa_wu = db.Column(db.Float, nullable=False)


#rutas ------------------------------------------------------------

#ruta principal
@app.route('/')
def index():
    ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()
    return render_template('index.html', ultima_tasa=ultima_tasa)

#ruta de prueba
@app.route('/login')
def login():
    return 'Login'

@app.route('/definir_tasas', methods=['GET', 'POST'])
def definir_tasas():
    if request.method == 'POST':

        # Convertir la cadena de fecha del formulario a un objeto date
        fecha_str = request.form['fecha']  # La cadena de fecha en formato 'DD/MM/YYYY'
        fecha_obj = datetime.strptime(fecha_str, '%d/%m/%Y').date()

        new = TasaDeCambio(
            fecha=fecha_obj,
            tasa_oficial=float(request.form['oficial']),
            tasa_compra=float(request.form['compra']),
            tasa_venta=float(request.form['venta']),
            tasa_wu=float(request.form['WU'])
        )
        db.session.add(new)
        db.session.commit()
        return redirect('/')

    return render_template('tasas.html')

#correrr la aplicación -------------------------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)