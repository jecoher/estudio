from flask import Flask, render_template, request, redirect
from base_datos import BaseDatos

app = Flask(__name__)

db = BaseDatos()

# Ruta principal que maneja ambos mundos (GET y POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    # CASO A: El usuario envió un formulario (Método POST)
    if request.method == 'POST':
        nombre_ingresado = request.form['nombre'].strip().upper()
        precio_ingresado = request.form['precio']
        cantidad_ingresado = request.form['cantidad']
        db.insertar_producto(nombre_ingresado, precio_ingresado, cantidad_ingresado)
        return redirect('/')
    
    # CASO B: El usuario solo entró a ver la página (Método GET)
    registros = db.obtener_todos()
    return render_template('index.html', elementos=registros)

@app.route('/eliminar/<int:id_producto>', methods=['POST'])
def eliminar(id_producto):
    db.eliminar_producto(id_producto)
    return redirect('/')

@app.route('/editar/<int:id_producto>', methods=['GET', 'POST'])
def editar(id_producto):
    # ... lógica para mostrar el formulario (POST) ...
    if request.method == 'POST':
        nuevo_nombre  = request.form['nombre'].strip().upper()
        nuevo_precio  = request.form['precio']
        nueva_cantidad  = request.form['cantidad']
        db.actualizar_producto(id_producto, nuevo_nombre, nuevo_precio, nueva_cantidad)
        return redirect('/')
    # ... lógica para mostrar el formulario (GET) ...
    producto = db.obtener_por_id(id_producto)
    return render_template('editar.html', producto=producto)



if __name__ == '__main__':
    app.run(debug=True)
    