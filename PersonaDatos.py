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
        elif "UNIQUE" in str(ex) and "dni" in str(ex):
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
    
   
    
def find(dniPersona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute ("SELECT * FROM personas WHERE dni='{dni}'".format(dniPersona=dniPersona))
        res = cursor.fetchall()
        if res:

            info=res[0]
            persona_info={"id":info[0], "dni":info[1], "Edad": info[2], "Nombre": info[3], "Apellidos": info[4], "Dirección":info[5], "Email":info[6]}
            
            return{"respuesta":True, "persona": persona_info, "mensaje":"Persona encontrada"}
        else:
            
            return{"respuesta":False, "mensaje":"NO existe la persona"}
    except Exception as ex:
        
        return {"respuesta": False, "mensaje":str(ex)}
    
    

def update(persona):
    try:
        db=con.conectar()
        cursor= db.cursor()
        persona= dict(persona)
        dniPersona= persona.get('dni')
        persona.pop('dni')
        valores= tuple(persona.value())
        sql= """
        UPDATE personas
        SET  
        Edad=?, 
        Nombre=?, 
        Apellidos=?, 
        Dirección=?, 
        Email=?
        WHERE dni='{dni}' 
        """.format(dni=dniPersona)
        cursor.execute(sql, (valores))
        modificada= cursor.rowcount>0
        db.commit()
        
        if modificada:
            return{"respuesta": modificada, "mensaje": "Persona actualizada" }
        else: 
            return{"respuesta": modificada, "mensaje": "No existe esa persona con ese dni" }
    except Exception as ex:
        return{"respuesta": False, "mensaje": str(ex)}
    

def delete(idPersona):
    try:
        db=con.conectar()
        cursor= db.cursor()
        
        sql= """
        DELETE FROM personas WHERE id='{id}'""".format(id=idPersona)
        cursor.execute(sql)
        eliminada= cursor.rowcount>0
        db.commit()
        
        if eliminada:
            return{"respuesta": eliminada, "mensaje": "Persona eliminada" }
        else: 
            return{"respuesta": eliminada, "mensaje": "No existe la persona con ese id" }
    except Exception as ex:
        return{"respuesta": False, "mensaje": str(ex)}
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

