import sqlite3

# clase de base de datos
class BaseDatos:
    def __init__(self, nombre_archivo='base.db'):
        self.nombre_archivo = nombre_archivo
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self.nombre_archivo)

    def crear_tabla(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad REAL NOT NULL

            )
''')
        conn.commit()
        conn.close()

    def insertar_producto(self, nombre, precio, cantidad, id=None):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (nombre, precio, cantidad) 
            VALUES (?,?,?)
        ''', (nombre, precio, cantidad))
        conn.commit()
        conn.close()

    def obtener_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, precio, cantidad FROM items')
        registros = cursor.fetchall()
        conn.close()
        return registros

    def eliminar_producto(self, id_producto):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = ?', (id_producto,))
        conn.commit()
        conn.close()

    def obtener_por_id(self, id_producto):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, precio, cantidad FROM items WHERE id = ?', (id_producto,))
        producto = cursor.fetchone()
        conn.close()        
        return producto

    def actualizar_producto(self, id_producto, nombre, precio, cantidad):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE items
            SET nombre = ?, precio = ?, cantidad = ?
            WHERE id = ?
''', (nombre, precio, cantidad, id_producto))
        conn.commit()
        conn.close()

    

