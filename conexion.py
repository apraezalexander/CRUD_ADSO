import sqlite3
def conectar(): 
    miConexion = sqlite3.connect("crud.db")
    cursor = miConexion.cursor()

    try: 
        sql= """
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DNI TEXT NOT NULL UNIQUE,
            Edad INTEGER NOT NULL,
            Nombre TEXT NOT NULL,
            Apellidos TEXT NOT NULL,
            Dirección TEXT DEFAULT "No tiene",
            Email TEXT NOT NULL UNIQUE 
        )
        """
        cursor.execute(sql)
        
        
        return miConexion
    except Exception as ex: 
        print("Error de conexion: ", ex) 
    finally:
        cursor.close()
        
    