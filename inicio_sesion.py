from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
from datetime import datetime
import platform

raiz=Tk()
raiz.title("Segundo formulario")
raiz.geometry("280x280")
raiz.resizable(0,0)

#----------CONECTAR BBDD---------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Marcelo231984",
    database="ITSM",
)
cursor=mydb.cursor()

#------------VARIABLES------------
miusuario=StringVar()
micontrasena=StringVar()

text_titulo=Label(text="Ingreso a ITSM", background="navy", foreground="white", width=250, font=("Calibri",22)).pack()
Label(text="").pack()
text_usuario=Label(text="Ingrese el nombre de usuario").pack()
Label(text="").pack()
cuadro_usuario=Entry(textvariable=miusuario).pack()
Label(text="").pack()
text_contrasena=Label(text="Ingrese su contraseña").pack()
Label(text="").pack()
cuadro_contrasena=Entry(textvariable=micontrasena, show='*').pack()
Label(text="").pack()


def iniciosesion():
    vargestion = (miusuario.get(), micontrasena.get())
    cursor.execute('SELECT CONTRASENA FROM usuarios WHERE SESION_USUARIO=%s AND CONTRASENA=%s', vargestion)
    
    if cursor.fetchall():
        fecha_sesion = datetime.today().strftime('%Y-%m-%d %H:%M')
        sistema_operativo = platform.platform()
        variablesacceso = (miusuario.get(), fecha_sesion, sistema_operativo)
        try:
            cursor.execute('INSERT INTO bitacora(sesion_usuario, last_loggin, sistema_operativo) VALUES(%s,%s,%s)',variablesacceso)
            mydb.commit()
            raiz.destroy()
            subprocess.call("Pantalla_Inicial.py", shell=True)
        except:
            messagebox.showinfo('Error', "Error al iniciar sesión")
    else:
        messagebox.showerror("Intento de ingreso", "Error la iniciar con usuario o contraseña")

#------------BOTONES------------
botoninicia=Button(text="Iniciar sesión",width=10,command=iniciosesion).pack()



raiz.mainloop()