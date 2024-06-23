import sqlite3


def nuevaContrasena(contrasena, cuenta):
    try:
        with sqlite3.connect("contraseñas.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS contraseñas (id INTEGER PRIMARY KEY AUTOINCREMENT, contraseña TEXT, cuenta_asociada TEXT)")
            conn.commit()
            cursor.execute("CREATE TABLE IF NOT EXISTS ids_eliminados (id INTEGER PRIMARY KEY);")
            conn.commit()
            cursor.execute("SELECT id FROM ids_eliminados ORDER BY id LIMIT 1")
            row = cursor.fetchone()
            if row:
                id_reutilizar = row[0]
                cursor.execute("DELETE FROM ids_eliminados WHERE id = ?", (id_reutilizar,))
            else:
                # No hay IDs en ids_eliminados, SQLite generará automáticamente el próximo ID
                id_reutilizar = None

            # Insertar en la tabla contraseñas utilizando el ID reutilizado o el nuevo ID generado automáticamente
            cursor.execute("INSERT INTO contraseñas (id, contraseña, cuenta_asociada) VALUES (?, ?, ?)",(id_reutilizar, contrasena, cuenta))
            conn.commit()

            print("Contraseña insertada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar contraseña: {e}")


def verTodasContrasena():
    try:
        with sqlite3.connect("contraseñas.sqlite") as conn:
            cursor = conn.cursor()
            for contrasena in cursor.execute("SELECT * FROM contraseñas"):
                print("id: " + str(contrasena[0]) + " | contraseña: " + contrasena[1] + " | cuenta asociada: " +
                      contrasena[2])
    except sqlite3.Error as e:
        print(f"Error al ver contraseñas: {e}")


def borrarContrasena():
    try:
        id = int(input("Ingrese id de la contraseña a borrar: "))
    except:
        print("Error. El valor ingresado debe ser un numero entero")
        exit()
    try:
        with sqlite3.connect("contraseñas.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ids_eliminados (id INTEGER PRIMARY KEY);")
            conn.commit()
            cursor.execute("SELECT id FROM contraseñas WHERE id = ?", (id,))
            contrasena = cursor.fetchone()
            if contrasena:
                cursor.execute("DELETE FROM contraseñas WHERE id = ?", (id,))
                conn.commit()
                cursor.execute("INSERT INTO ids_eliminados (id) VALUES (?)", (id,))
                conn.commit()
                print("Contraseña eliminada correctamente.")
            else:
                print("No se encontró la contraseña a borrar.")
    except sqlite3.Error as e:
        print(f"Error al eliminar contraseña: {e}")


def buscarContrasena(cuenta):
    try:
        with sqlite3.connect("contraseñas.sqlite") as conn:
            cursor = conn.cursor()
            encontrado = cursor.execute(f"SELECT * FROM contraseñas WHERE cuenta_asociada == {cuenta}")
            if encontrado:
                encontrado.fetchall()
            else:
                print("No se encontro la cuenta")
    except sqlite3.Error as e:
        print(f"Error al buscar contraseña: {e}")
