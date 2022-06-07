from tkinter import simpledialog
from matplotlib.pyplot import show
import mysql.connector
import os
from tkinter import *
from tkinter import messagebox
import subprocess

raiz=Tk()
raiz.title("Pantalla de inicio")
barramenu=Menu(raiz)
raiz.config(menu=barramenu,width=300, height=300)
raiz.geometry("800x800")
raiz.resizable(0,0)

#----------CONECTAR BBDD---------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Marcelo231984",
    database="ITSM",
)
cursor=mydb.cursor()

#------------FUNCIONES------------
def respaldoBBDD():
    ingresapass = simpledialog.askstring("WARNING!","Favor ingrese la contraseña de la BBDD", show='*')
    if ingresapass == "Marcelo231984":
        database = "ITSM"
        os.popen('mysqldump -h %s -u %s -p%s %s > %s.sql' % ("localhost","root", ingresapass,database,database+"_backup"))
        messagebox.showinfo("Respaldo", "El respaldo se ha realizado correctamente")
    else:
        messagebox.showerror("Error", "La contraseña ingresada no corresponde")

def restauraBBDD():
    validarrestaura = messagebox.askquestion("Advertencia!", "¿Está seguro que desa restaurar la base de datos?")
    if validarrestaura == "yes":
        ingresapass = simpledialog.askstring("WARNING!","Favor ingrese la contraseña de la BBDD", show='*')
        if ingresapass == "Marcelo231984":
            database = "ITSM"
            os.popen('mysql -h %s -u %s -p%s %s < %s.sql' % ("localhost","root", ingresapass,database,database+"_backup"))
            messagebox.showinfo("Restauración", "La restauración se ha realizado correctamente")
        else:
            messagebox.showerror("Error", "La contraseña ingresada no corresponde")

def menubitacorau():
    subprocess.call("tree_view.py", shell=True)

def salir():
    salida=messagebox.askquestion("Salir", "Desea salir de la aplicación")
    if salida=="yes":
        raiz.destroy()

def menuayudar():
    subprocess.call("menu_ayuda.py", shell=True)

def usuarios():
    subprocess.call("prueba_ITSM.py", shell=True)

#--------------MENÚS------------
menubbdd=Menu(barramenu, tearoff=0)
menubbdd.add_command(label="Respaldar BBDD", command=respaldoBBDD)
menubbdd.add_command(label="Restaurar BBDD", command=restauraBBDD)

menuusuarios=Menu(barramenu, tearoff=0)
menuusuarios.add_command(label="Usuarios", command=usuarios)

menubitacora=Menu(barramenu, tearoff=0)
menubitacora.add_command(label="Bitácora", command=menubitacorau)

menusalir=Menu(barramenu, tearoff=0)
menusalir.add_command(label="Salir", command=salir)

menuayuda=Menu(barramenu, tearoff=0)
menuayuda.add_command(label="Ayuda", command=menuayudar)

barramenu.add_cascade(label="BBDD", menu=menubbdd)
barramenu.add_cascade(label="Usuarios", menu=menuusuarios)
barramenu.add_cascade(label="Bitácora", menu=menubitacora)
barramenu.add_cascade(label="Ayuda", menu=menuayuda)
barramenu.add_cascade(label="Salir", menu=menusalir)


raiz.mainloop()