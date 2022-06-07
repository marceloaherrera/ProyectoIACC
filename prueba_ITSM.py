from tkinter import simpledialog
from matplotlib.pyplot import show
import mysql.connector
import re
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from numpy import place

raiz=Tk()
raiz.title("Primer formulario")
barramenu=Menu(raiz)
raiz.config(menu=barramenu,width=300, height=300)
raiz.resizable(0,0)
miframe=Frame(raiz, width=1200, height=500)
miframe.pack()
miframe2=Frame(raiz, width=1200, height=500)
miframe2.pack()

#----------CONECTAR BBDD---------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Marcelo231984",
    database="ITSM",
)
cursor=mydb.cursor()

#------------VARIABLES------------
miid=StringVar()
minombre=StringVar()
miapellido=StringVar()
miactivo=StringVar()
micorreo=StringVar()
miperfil=StringVar()
midireccion=StringVar()
mipassword=StringVar()

#------------FUNCIONES------------
def codigolimpia():
    miid.set("")
    minombre.set("")
    miapellido.set("")
    miactivo.set("")
    micorreo.set("")
    miperfil.set("")
    midireccion.set("")
    mipassword.set("")

def codigocrea():
    if len(cuadroid.get()) == 0:
        nombre = cuadronombre.get()
        apellido = cuadroapellido.get()
        correo = cuadrocorreo.get()
        direccion = cuadrodireccion.get()
        validaremail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        valida = re.search(validaremail,correo)
        if len(nombre) == 0 or nombre.isdigit() or len(apellido) == 0 or apellido.isdigit() or len(direccion) < 2 or len(cuadropassword.get()) <= 4:
            messagebox.showwarning("Advertencia", "Hay un campo vacío, tiene números o es demasiado corto")
        elif valida:
            #if cursor.execute('SELECT COUNT(correo) FROM usuarios WHERE correo='+cuadrocorreo.get()) <= 0:
            try:
                varGestion = (minombre.get(), miapellido.get(), miactivo.get(), micorreo.get(), miperfil.get(), midireccion.get(), mipassword.get(), minombre.get()+"."+miapellido.get())
                cursor.execute('INSERT INTO usuarios(NOMBRE, APELLIDO, ACTIVO, CORREO, PERFIL, UBICACIÓN, CONTRASENA, SESION_USUARIO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', varGestion)    
                mydb.commit()
                messagebox.showinfo("Insertar", "Realizado con éxito")
            except:
                messagebox.showerror("Error", "No se pudieron insertar los datos")
            #else: 
                #messagebox.showinfo("Advertencia", "Este correo ya existe, no se puede agregar usuario")
        else:
            messagebox.showwarning("Advertencia", "No es un email valido")
    else:
        messagebox.showwarning("Advertencia", "El cuadro ID se autocompletará, no se deben ingresar datos")

def codigolee():
    try:
        cursor.execute('SELECT * FROM usuarios WHERE ID_SESION='+miid.get())
        obtener=cursor.fetchall()
        for datos in obtener:
            minombre.set(datos[1])
            miapellido.set(datos[2])
            miactivo.set(datos[3])
            micorreo.set(datos[4])
            miperfil.set(datos[5])
            midireccion.set(datos[6])
        mydb.commit()
        messagebox.showinfo("Informativo", "Se obtuvieron los datos solicitados")
    except:
        messagebox.showerror("Error", "No se pudo obtener la información con los datos ingresados")

def codigoactualiza():
    nombre = cuadronombre.get()
    apellido = cuadroapellido.get()
    correo = cuadrocorreo.get()
    direccion = cuadrodireccion.get()
    validaremail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    valida = re.search(validaremail,correo)
    if len(nombre) == 0 or nombre.isdigit() or len(apellido) == 0 or apellido.isdigit() or len(direccion) < 2 or len(cuadropassword.get()) <= 4:
        messagebox.showwarning("Advertencia", "Hay un campo vacío, tiene números o es demasiado corto")
    elif valida:
        try:
            varGestion = (minombre.get(), miapellido.get(), miactivo.get(), micorreo.get(), miperfil.get(), midireccion.get(), mipassword.get())
            cursor.execute("UPDATE usuarios SET NOMBRE=%s, APELLIDO=%s, ACTIVO=%s, CORREO=%s, PERFIL=%s, UBICACIÓN=%s, CONTRASENA=%s WHERE ID_SESION="+miid.get(), varGestion)
            mydb.commit()
            messagebox.showinfo("Actualizar", "Actualización realizada con éxito")
            codigolimpia()
        except:
            messagebox.showerror("Error", "No se pudieron actualizar los datos")
    else:
        messagebox.showwarning("Advertencia", "No es un email valido")

def codigoelimina():
    if len(cuadroid.get()) == 0:
        messagebox.showwarning("Advertencia", "Debe ingresar un código de usuario")
    else:
        try:
            cursor.execute('DELETE FROM usuarios WHERE ID_SESION='+miid.get())
            mydb.commit()    
            messagebox.showinfo("Eliminar", "Realizado con éxito")
            codigolimpia()
        except:
            messagebox.showerror("Error", "No se pudieron eliminar los datos los datos")

""" def respaldoBBDD():
    ingresapass = simpledialog.askstring("WARNING!","Favor ingrese la contraseña de la BBDD", show='*')
    if ingresapass == "Marcelo231984":
        database = "ITSM"
        os.popen('mysqldump -h %s -u %s -p%s %s > %s.sql' % ("localhost","root", ingresapass,database,database+"_backup"))
        #subprocess.Popen('mysqldump -h localhost -u root -p Marcelo231984 ITSM > ITSM.sql', shell=True)
        #"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump" -h localhost -u root -p ITSM > ITSM_B.sql
        messagebox.showinfo("Respaldo", "El respaldo se ha realizado correctamente")
    else:
        messagebox.showerror("Error", "La contraseña ingresada no corresponde") """
    
""" def restauraBBDD():
    validarrestaura = messagebox.askquestion("Advertencia!", "¿Está seguro que desa restaurar la base de datos?")
    if validarrestaura == "yes":
        ingresapass = simpledialog.askstring("WARNING!","Favor ingrese la contraseña de la BBDD", show='*')
        if ingresapass == "Marcelo231984":
            database = "ITSM"
            os.popen('mysql -h %s -u %s -p%s %s < %s.sql' % ("localhost","root", ingresapass,database,database+"_backup"))
            messagebox.showinfo("Restauración", "La restauración se ha realizado correctamente")
        else:
            messagebox.showerror("Error", "La contraseña ingresada no corresponde") """

def salir():
    salida=messagebox.askquestion("Salir", "Desea salir de la aplicación")
    if salida=="yes":
        raiz.destroy()

#--------------MENÚS------------
""" menubbdd=Menu(barramenu, tearoff=0)
menubbdd.add_command(label="Respaldar BBDD", command=respaldoBBDD)
menubbdd.add_command(label="Restaurar BBDD", command=restauraBBDD)
 """
menulimpiar=Menu(barramenu, tearoff=0)
menulimpiar.add_command(label="Limpiar campos", command=codigolimpia)

menusalir=Menu(barramenu, tearoff=0)
menusalir.add_command(label="Salir", command=salir)

""" barramenu.add_cascade(label="BBDD", menu=menubbdd) """
barramenu.add_cascade(label="Limpiar", menu=menulimpiar)
barramenu.add_cascade(label="Salir", menu=menusalir)

#------------CUADROS------------
cuadroid=Entry(miframe, textvariable=miid)#, state=DISABLED) deshabilita el textbox
cuadroid.grid(row=0, column=1, pady=10, padx=10)
cuadroid.config(justify="left")
cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=1, column=1, pady=10, padx=10)
cuadronombre.config(justify="left")
cuadroapellido=Entry(miframe, textvariable=miapellido)
cuadroapellido.grid(row=2, column=1, pady=10, padx=10)
cuadroapellido.config(justify="left")
cuadroactivo=ttk.Combobox(miframe, textvariable=miactivo, values=["Si", "No"])
cuadroactivo.grid(row=3, column=1, pady=10, padx=10)
cuadroactivo.config(justify="left")#, show="*")
cuadroactivo.current(0)
cuadrocorreo=Entry(miframe, textvariable=micorreo)
cuadrocorreo.grid(row=4, column=1, pady=10, padx=10)
cuadrocorreo.config(justify="left")
cuadroperfil=ttk.Combobox(miframe, textvariable=miperfil, values=["Administrador", "Técnico", "Usuario"])
cuadroperfil.grid(row=5, column=1, pady=10, padx=10)
cuadroperfil.config(justify="left")
cuadroperfil.current(0)
cuadrodireccion=Entry(miframe, textvariable=midireccion)
cuadrodireccion.grid(row=6, column=1, pady=10, padx=10)
cuadrodireccion.config(justify="left")
cuadropassword=Entry(miframe, textvariable=mipassword, show="*")
cuadropassword.grid(row=7, column=1, pady=10, padx=10)
cuadropassword.config(justify="left")

nombrelabel=Label(miframe, text="ID: ")
nombrelabel.grid(row=0,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Nombre: ")
nombrelabel.grid(row=1,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Apellido: ")
nombrelabel.grid(row=2,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Activo: ")
nombrelabel.grid(row=3,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Correo: ")
nombrelabel.grid(row=4,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Perfil: ")
nombrelabel.grid(row=5,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Dirección: ")
nombrelabel.grid(row=6,column=0,sticky="e",pady=10, padx=10)
nombrelabel=Label(miframe, text="Contraseña: ")
nombrelabel.grid(row=7,column=0,sticky="e",pady=10, padx=10)

#------------BOTONES------------
botoncrear=Button(miframe2,text="Crear",width=7,command=codigocrea)
botoncrear.grid(row=0,column=0,pady=5, padx=5)
botonleer=Button(miframe2,text="Leer",width=7,command=codigolee)
botonleer.grid(row=0, column=1,pady=5, padx=5)
botonactualizar=Button(miframe2,text="Actualizar",width=7, command=codigoactualiza)
botonactualizar.grid(row=0, column=2,pady=5, padx=5)
botoneliminar=Button(miframe2,text="Eliminar",width=7,command=codigoelimina)
botoneliminar.grid(row=0, column=3,pady=5, padx=5)


raiz.mainloop()