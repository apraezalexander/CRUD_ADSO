import sqlite3
def conectar(): 
    miConexion = sqlite3.connect("crud.db")
    cursor = miConexion.cursor()

    try: 
        sql= """
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni TEXT NOT NULL UNIQUE,
            Nombre TEXT NOT NULL,
            Apellidos TEXT NOT NULL,
            Edad INTEGER NOT NULL,
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
        
    