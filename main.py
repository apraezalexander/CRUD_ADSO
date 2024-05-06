from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PersonaDatos as pDatos

#ventaja 
v= Tk()
v.title("Aplicación CRUD")
ancho=450
alto=400
x_v = v.winfo_screenwidth() // 2 - ancho //2
y_v = v.winfo_screenheight() // 2 - ancho // 2
pos = str(ancho)+ "x"+str(alto)+"+"+str(x_v)+"+"+str(y_v)
v.geometry(pos)
v.state("zoomed")
v.configure(bg="#fff")

#### --------------VARIABLES------------- ####
txt_id= StringVar()
txt_dni= StringVar()
txt_edad= StringVar()
txt_nombre= StringVar()
txt_apellidos= StringVar()
txt_direccion= StringVar()
txt_email= StringVar()

#### --------------FUNCIONES------------- ####

def creditos():
    messagebox.showinfo("Créditos", 
                        """
                        Creado por: 
                        Alexander Apraez
                        Aprendiz SENA
                        Analisis y Desarrollo de Software 
                        ----------------------------------
                        - Linkedin: apraezalexander
                        - Email: al.apraez@hotmail.com
                        ----------------------------------
                        """)

def salir ():
    res=messagebox.askquestion("salir", "¿Desea salir de la aplicación?")
    if res=="yes":
        v.destroy()

def llenartabla():
    table.delete(*table.get_children())

    res= pDatos.findALL()
    personas = res.get("personas")
    for fila in personas:
        row= list(fila)
        row.pop(0)
        row = tuple(row)
        table.insert("", END, text=id, values=row)

def limpiarCampos():
    txt_dni.set("")
    txt_nombre.set("")
    txt_apellidos.set("")
    txt_edad.set("")
    txt_direccion.set("")
    txt_email.set("")
    e_dni.focus()

    
def guardar():                     
    if txt_edad.get().isnumeric():
        per= {"dni": txt_dni.get(), "Nombre": txt_nombre.get(), "Apellidos": txt_apellidos.get(), "Edad": int(txt_edad.get()), "Dirección": txt_direccion.get(), "Email": txt_email.get()}
        res= pDatos.save(per)
        if res.get("respuesta"):
            llenartabla()
            messagebox.showinfo("OK", res.get("mensaje"))
            limpiarCampos()
        else:
            messagebox.showerror("Lo siento", res.get("mensaje"))
    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Lo siento","La edad debe ser un número")

def consultar():
    if txt_dni.get()!="":
        res = pDatos.find(txt_dni.get())
        if res.get("respuesta"):
            persona= res.get("persona")
            txt_nombre.set(persona.get("Nombre"))
            txt_apellidos.set(persona.get("Apellidos"))
            txt_edad.set(persona.get("Edad"))
            txt_direccion.set(persona.get("Dirección"))
            txt_email.set(persona.get("Email"))
        else:
            e_dni.focus()
            limpiarCampos()
            messagebox.showerror("Lo siento", "No existe la persona")
    else:
        e_dni.focus()
        limpiarCampos()
        messagebox.showerror("Lo siento", "Debe ingresar el DNI")

def actualizar():                     
    if txt_edad.get().isnumeric():
        per= {"dni": txt_dni.get(), "Nombre": txt_nombre.get(), "Apellidos": txt_apellidos.get(), "Edad": int(txt_edad.get()), "Dirección": txt_direccion.get(), "Email": txt_email.get()}
        res= pDatos.update(per)
        if res.get("respuesta"):
            llenartabla()
            messagebox.showinfo("OK", res.get("mensaje"))
            limpiarCampos()
        else:
            messagebox.showerror("Lo siento", res.get("mensaje"))
    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Lo siento","La edad debe ser un número")

def eliminar():                     
    if txt_dni.get()!="":
        res= pDatos.find(txt_dni.get())
        if res.get("respuesta"):
            persona = res.get("persona")
            respuesta = messagebox.askquestion("Confirmar", "Realmente desea eliminar a {Nombre} {Apellidos}".format(Nombre=persona.get("Nombre"), Apellidos=persona.get("Apellidos")))
            if respuesta== "yes":
                res= pDatos.delete(persona.get("id"))
                if res.get("respuesta"):
                    llenartabla()
                    limpiarCampos()
                    messagebox.showinfo("OK", res.get("mensaje"))
                else:
                    messagebox.showwarning("Lo siento!", "No se logró eliminar a la persona"+res.get("mensaje"))
        else:
            messagebox.showwarning("Lo siento!", "No existe la persona")
            limpiarCampos()
    else:
        e_dni.focus()
        messagebox.showerror("Lo siento","Debe ingresar el DNI")
#### --------------FIN FUNCIONES------------- ####

#### --------------GUI------------- ####
fuente= ("verdana", 12)
Label(v, text="DNI:", anchor="w", justify="left", width=10, bg="lightgreen", font=fuente).grid(row=0, column=0, padx=10, pady=5)
Label(v, text="Nombre:", anchor="w", justify="left", width=10, bg="lightgreen", font=fuente).grid(row=1, column=0, padx=10, pady=5)
Label(v, text="Apellidos:", anchor="w", justify="left", width=10, bg="lightgreen", font=fuente).grid(row=2, column=0, padx=10, pady=5)
Label(v, text="Edad:", anchor="w", justify="left", width=10, bg="lightgreen", font=fuente).grid(row=3, column=0, padx=10, pady=5)
Label(v, text="Dirección:", anchor="w", justify="left", width=10, bg="lightgreen", font=fuente).grid(row=4, column=0, padx=10, pady=5)
Label(v, text="Email:", anchor="w", justify="left", width=10, bg="lightgreen", font=fuente).grid(row=5, column=0, padx=10, pady=5)

###Inputs###
e_dni= ttk.Entry(v, font=fuente, textvariable=txt_dni)
e_nombre= ttk.Entry(v, font=fuente, textvariable=txt_nombre)
e_apellidos= ttk.Entry(v, font=fuente, textvariable=txt_apellidos)
e_edad= ttk.Entry(v, font=fuente, textvariable=txt_edad)
e_direccion= ttk.Entry(v, font=fuente, textvariable=txt_direccion)
e_email= ttk.Entry(v, font=fuente, textvariable=txt_email)

e_dni.grid(row=0, column=1)
e_nombre.grid(row=1, column=1)
e_apellidos.grid(row=2, column=1)
e_edad.grid(row=3, column=1)
e_direccion.grid(row=4, column=1)
e_email.grid(row=5, column=1)

##-----imágenes de íconos---####

iconNew= PhotoImage(file="new.png")
iconrefresh= PhotoImage(file="refresh.png")
iconfind= PhotoImage(file="find.png")
icondelete= PhotoImage(file="delete.png")



###--BOTONES--###
ttk.Button(v, text="Guardar", command=guardar,image=iconNew, compound=LEFT).place(x=10, y=210)
ttk.Button(v, text="Consultar", command=consultar, image=iconfind, compound=LEFT).place(x=120, y=210)
ttk.Button(v, text="Actualizar", command=actualizar, image=iconrefresh, compound=LEFT).place(x=230, y=210)
ttk.Button(v, text="Eliminar", command=eliminar, image=icondelete, compound=LEFT).place(x=340, y=210)

###--- CREACIÓN DE TABLAS---####

Label(v, text="LISTADO DE PERSONAS", font=("Arial", 16), bg="#fff").place(x=700, y=5)
table=ttk.Treeview(v)
table.place(x=450, y=40)
table["columns"] = ("DNI", "NOMBRE", "APELLIDOS", "EDAD", "DIRECCION", "CORREO")
table.column("#0", width=0, stretch=NO)
table.column("DNI", width=100, anchor=CENTER)
table.column("NOMBRE", width=150, anchor=CENTER)
table.column("APELLIDOS", width=160, anchor=CENTER)
table.column("EDAD", width=100, anchor=CENTER)
table.column("DIRECCION", width=180, anchor=CENTER)
table.column("CORREO", width=180, anchor=CENTER)
table.heading("#0", text="")
table.heading("DNI", text="DNI")
table.heading("NOMBRE", text="NOMBRE")
table.heading("APELLIDOS", text="APELLIDOS")
table.heading("EDAD", text="EDAD")
table.heading("DIRECCION", text="DIRECCIÓN")
table.heading("CORREO", text="CORREO")

####---- MENU PRINCIPAL-----####

menuTop = Menu(v)

v.config(menu= menuTop)
m_archivo = Menu(menuTop, tearoff=0)
m_archivo.add_command(label="Créditos", command=creditos)
m_archivo.add_command(label="Salir", command=salir)
menuTop.add_cascade(label="Archivo", menu=m_archivo)

m_limpiar = Menu(menuTop, tearoff=0)
m_limpiar.add_command(label="Limpiar campos", command=limpiarCampos)
menuTop.add_cascade(label="Limpiar", menu=m_limpiar)

m_crud = Menu(menuTop, tearoff=0)
m_crud.add_command(label="Guardar",command=guardar, image=iconNew, compound=LEFT)
m_crud.add_command(label="Consultar", command=consultar, image=iconfind, compound=LEFT)
m_crud.add_command(label="Actualizar", command=actualizar, image=iconrefresh, compound=LEFT)
m_crud.add_command(label="Eliminar", command=eliminar, image=icondelete, compound=LEFT)
menuTop.add_cascade(label="Crud", menu=m_crud)



e_dni.focus()

llenartabla()

v.mainloop()