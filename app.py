#paqueterías externas ---------------------------------------------
from flask import Flask, render_template, redirect, url_for, request, render_template_string, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker #Agregado por Rigoberto

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

# Definición del modelo de la Tabla MUC
class MUC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agencia = db.Column(db.String(50), nullable=False)
    codigo_contable = db.Column(db.String(50), nullable=False)
    nombre_cuenta = db.Column(db.String(100), nullable=False)
    clasificacion_cuenta = db.Column(db.String(50), nullable=False)
    nivel_cuenta = db.Column(db.Integer, nullable=False)

@app.route('/search', methods=['POST'])
def search():
    term = request.form['term']
    results = MUC.query.filter(MUC.nombre_cuenta.like(f'%{term}%')).all()
    accounts = [{'id': muc.id, 'nombre_cuenta': muc.nombre_cuenta} for muc in results]
    return jsonify(accounts)    

    def __repr__(self):
        return f'<MUC {self.nombre_cuenta}>'

# Crear la tabla usuarios

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///control_caja.db'
#db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nivel_permiso = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

# Creacion de la tabla OP_WU
class OpWu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaccion = db.Column(db.String(80), nullable=False)
    tipo_operacion = db.Column(db.String(80), nullable=False)
    montotrus = db.Column(db.Float, nullable=False)
    montopus = db.Column(db.Float, nullable=False)
    montotrcs = db.Column(db.Float, nullable=False)
    montopcs = db.Column(db.Float, nullable=False)
    ib1000cs = db.Column(db.Float, nullable=False)
    ib500cs = db.Column(db.Float, nullable=False)
    ib200cs = db.Column(db.Float, nullable=False)
    ib100cs = db.Column(db.Float, nullable=False)
    ib50cs = db.Column(db.Float, nullable=False)
    ib20cs = db.Column(db.Float, nullable=False)
    ib10cs = db.Column(db.Float, nullable=False)
    ib5cs = db.Column(db.Float, nullable=False)
    ib1cs = db.Column(db.Float, nullable=False)
    sb1000cs = db.Column(db.Float, nullable=False)
    sb500cs = db.Column(db.Float, nullable=False)
    sb200cs = db.Column(db.Float, nullable=False)
    sb100cs = db.Column(db.Float, nullable=False)
    sb50cs = db.Column(db.Float, nullable=False)
    sb20cs = db.Column(db.Float, nullable=False)
    sb10cs = db.Column(db.Float, nullable=False)
    sb5cs = db.Column(db.Float, nullable=False)
    sb1cs = db.Column(db.Float, nullable=False)
    eb100us = db.Column(db.Float, nullable=False)
    eb50us = db.Column(db.Float, nullable=False)
    eb20us = db.Column(db.Float, nullable=False)
    eb10us = db.Column(db.Float, nullable=False)
    eb5us = db.Column(db.Float, nullable=False)
    eb1us = db.Column(db.Float, nullable=False)
    pb100us = db.Column(db.Float, nullable=False)
    pb50us = db.Column(db.Float, nullable=False)
    pb20us = db.Column(db.Float, nullable=False)
    pb10us = db.Column(db.Float, nullable=False)
    pb5us = db.Column(db.Float, nullable=False)
    pb1us = db.Column(db.Float, nullable=False)
    ajuste = db.Column(db.Float, nullable=False)

    # Puedes agregar más campos según necesites

from flask import request, redirect, url_for, flash

@app.route('/operaciones_wu', methods=['GET', 'POST'])
def operaciones_wu():
    if request.method == 'POST':
        try:
            nueva_operacion = OpWu(
            transaccion=request.form['transaccion'],
            tipo_operacion=request.form['tipo_operacion'],
            montotrus=float((request.form['montotrus']),0),
            montopus = float((request.form['montopus']), 0),            
            montotrcs=float((request.form['montotrcs']),0),
            montopcs=float((request.form['montopcs']), 0),
            ib1000cs=float((request.form['ib1000cs']),0),
            ib500cs=float((request.form['ib500cs']),0),
            ib200cs=float((request.form['ib200cs']),0),
            ib100cs=float((request.form['ib100cs']),0),
            ib50cs=float((request.form['ib50cs']),0),
            ib20cs=float((request.form['ib20cs']),0),
            ib10cs=float((request.form['ib10cs']),0),
            ib5cs=float((request.form['ib5cs']),0),
            ib1cs=float((request.form['ib1cs']),0),
            sb1000cs=float((request.form['sb1000cs']),0),
            sb500cs=float((request.form['sb500cs']),0),
            sb200cs=float((request.form['sb200cs']),0),
            sb100cs=float((request.form['sb100cs']),0),
            sb50cs=float((request.form['sb50cs']),0),
            sb20cs=float((request.form['sb20cs']),0),
            sb10cs=float((request.form['sb10cs']),0),
            sb5cs=float((request.form['sb5cs']),0),
            sb1cs=float((request.form['sb1cs']),0),
            eb100us=float((request.form['eb100us']),0),
            eb50us=float((request.form['eb50us']),0),
            eb20us=float((request.form['eb20us']),0),
            eb10us=float((request.form['eb10us']),0),
            eb5us=float((request.form['eb5us']),0),
            eb1us=float((request.form['eb1us']),0),
            pb100us=float((request.form['pb100us']),0),
            pb50us=float((request.form['pb50us']),0),
            pb20us=float((request.form['pb20us']),0),
            pb10us=float((request.form['pb10us']),0),
            pb5us=float((request.form['pb5us']),0),
            pb1us=float((request.form['pb1us']),0),
            ajuste = float(request.form.get('ajuste', 0))
            )
            db.session.add(nueva_operacion)
            db.session.commit()
            flash('Operación guardada con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al guardar la operación: ' + str(e), 'danger')
        finally:
            return redirect(url_for('operaciones_wu'))  # Asegúrate de redirigir o renderizar una plantilla aquí

            #except ValueError:
            # Maneja el caso en que el valor no sea convertible a float
            #print("El valor proporcionado para 'ajuste' no es un número válido.")
        
        ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()
        return render_template('operaciones_wu.html', ultima_tasa=ultima_tasa)
        

@app.route('/reporte_caja')
def reporte_caja():
    operaciones = OpWu.query.all()  # Consulta todos los registros de la tabla OpWu
    return render_template('reporte_caja.html', operaciones=operaciones)


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

#ruta para definir tasas de cambio
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

#ruta para calcular el cambio
@app.route('/calcular_cambio',methods=['GET', 'POST'])
def calcular_cambio():
    if request.method == 'POST':
        tipo_cambio = request.form.get('tipo_cambio')
        monto = float(request.form.get('monto'))

        # Obtener el último registro de TasaDeCambio
        ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()

        if tipo_cambio == 'venta':
            tasa = ultima_tasa.tasa_venta
        elif tipo_cambio == 'compra':  # compra
            tasa = ultima_tasa.tasa_compra

        # Calcular el cambio
        cambio = monto * tasa

        return render_template('resultado_cambio.html', cambio=cambio, monto=monto, tipo_cambio=tipo_cambio)

    return render_template('calcular_cambio.html')

#ruta para agregar nuevo registro
@app.route('/nuevo_registro', methods=['GET', 'POST'])
def nuevo_registro():
    ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()
    if request.method == 'POST':
        return render_template('nuevo_registro.html',tasa=ultima_tasa)
    else:
        return render_template('nuevo_registro.html',tasa=ultima_tasa)
       
       
#Ruta para agregar usuarios
    from flask import request, redirect, url_for

@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        nivel_permiso = request.form['nivel_permiso']

        nuevo_usuario = Usuario(nombre=nombre, email=email, nivel_permiso=nivel_permiso)
        
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for('index'))  # Redireccionar a la página de inicio o a donde prefieras

    return render_template('agregar_usuario.html')


#ruta para generar reporte
@app.route('/generar_reporte')
def generar_reporte():
    return render_template('generar_reporte.html')

#ruta para Agregrar Cuentas Contables
@app.route('/formulario_muc', methods=['GET', 'POST'])
def formulario_muc():

    return render_template('formulario_muc.html')


#ruta para el manejo de caja
@app.route('/manejo_caja',)
def manejo_caja():
    return render_template('manejo_caja.html')

#ruta para acceder al historial de la base de registros
@app.route('/base_registros')
def base_registros():
    return render_template('base_registros.html')

#ruta para acceder a factura
@app.route('/factura')
def factura():
    return render_template('factura.html')

#ruta para acceder al Comprobante de Diario
@app.route('/cdiario')
def cdiario():
    return render_template('cdiario.html')

#ruta para acceder a Crear las agencias
@app.route('/agencias')
def agencias():
    return render_template('agencias.html')

#ruta para acceder al MUC Manual Unico de Cuentas
from flask import request, redirect, url_for

@app.route('/agregar_muc', methods=['POST'])
def agregar_muc():
    if request.method == 'POST':
        agencia = request.form['agencia']
        codigo_contable = request.form['codigo_contable']
        nombre_cuenta = request.form['nombre_cuenta']
        clasificacion_cuenta = request.form['clasificacion_cuenta']
        nivel_cuenta = request.form['nivel_cuenta']

        nuevo_muc = MUC(agencia=agencia, codigo_contable=codigo_contable, nombre_cuenta=nombre_cuenta, clasificacion_cuenta=clasificacion_cuenta, nivel_cuenta=int(nivel_cuenta))
        
        db.session.add(nuevo_muc)
        db.session.commit()

        return redirect(url_for('muc_reporte'))

@app.route('/muc_reporte')
def muc_reporte():
    todos_los_muc = MUC.query.all()
    return render_template('reporte_muc.html', muc=todos_los_muc)


#ruta para acceder a agregar nuevo cliente
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

#ruta para acceder a agregar Cuenta en el muc
@app.route('/ingresar_muc')
def ingresar_muc():
    return render_template('ingresar_muc.html')

@app.route('/muc')
def muc():
    return render_template('muc.html')

@app.route('/agregar_usuarios')
def agregar_usuarios():
    return render_template('agregar_usuarios.html')

@app.route('/buscar_cuenta')
def buscar_cuenta():
    return render_template('buscar_cuenta.html')

#@app.route('/operaciones_wu')
#def operaciones_wu():
 #   ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()
  #  return render_template('operaciones_wu.html', ultima_tasa=ultima_tasa)

@app.route('/operaciones_wu_ca')
def operaciones_wu_ca():
    ultima_tasa = TasaDeCambio.query.order_by(TasaDeCambio.id.desc()).first()
    return render_template('operaciones_wu_ca.html', ultima_tasa=ultima_tasa)

@app.route('/tasas')
def tasas():
    return render_template('tasas.html')

@app.route('/form')
def form():
    return render_template('form.html')

#Registrar Usuario
@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    return render_template('/auth/register.html')

#correrr la aplicación -------------------------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)