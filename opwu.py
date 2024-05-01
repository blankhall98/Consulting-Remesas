#paqueterías externas ---------------------------------------------
from flask import Flask, render_template, redirect, url_for, request, render_template_string, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker #Agregado por Rigoberto
from app import app, db, TasaDeCambio

#inicializar la aplicación ---------------------------------------
app = Flask(__name__)

#configuración de la base de datos --------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///control_caja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#ruta principal
@app.route('/')
def home():
    ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()
    return render_template('home.html', ultima_tasa=ultima_tasa)

@app.route('/operaciones_wu')
def operaciones_wu():
    return render_template('operaciones_wu.html')