import conexion as con

def save(persona):
    persona= dict(persona)
    cursor = None
    db = None

    try: 
        db=con.conectar()
        cursor=db.cursor()
        columnas = tuple(persona.keys())
        valores = tuple(persona.values())
        sql = """
        INSERT INTO personas{campos} values(?,?,?,?,?,?)
        """.format(campos=columnas)
        
        cursor.execute(sql,valores)
        creada= cursor.rowcount>0
        db.commit()
        if creada:
            
            return {"respuesta": creada, "mensaje":"Persona registrada"}
        else:
            
            return  {"respuesta": creada, "mensaje":"No se logró registrar a la persona"}
    except Exception as ex:
        if "UNIQUE" in str(ex) and "Email" in str(ex):
            mensaje= "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "DNI" in str(ex):
            mensaje= "Ya existe una persona con ese DNI"
        else: 
            mensaje = str(ex)
        
        return {"respuesta": False, "mensaje":mensaje}
    

def findALL():
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
        if personas: 
            
            return{"respuesta":True, "personas": personas, "mensaje":"Listado ok"}
        else:
            
            return{"respuesta":False, "mensaje":"NO hay personas registradas aún"}
    except Exception as ex:
        
        return {"respuesta": False, "mensaje":str(ex)}
    
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()
    