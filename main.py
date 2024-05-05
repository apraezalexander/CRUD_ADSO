import PersonaDatos as per

persona= {
          "DNI": "1234", 
          "Nombre": "camilo", 
          "Edad": 14,
          "Apellidos": "alvarez", 
          "Dirección": "pasto-nariño",
          "Email":"al.apraez@hotmail.com"}
res=per.save(persona)
print(res)