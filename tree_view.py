from tkinter import ttk
import mysql.connector
from tkinter import *

raiz=Tk()
raiz.title("Bitácora usuarios")
raiz.geometry("460x270")
raiz.resizable(0,0)

#----------CONECTAR BBDD---------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Marcelo231984",
    database="ITSM",
)
cursor=mydb.cursor()

#def leerdatos():
arbol = ttk.Treeview(raiz, selectmode ='browse')
arbol.grid(row=1,column=1,padx=20,pady=20)
arbol["columns"] = ("1", "2", "3",)
arbol['show'] = 'headings'

arbol.column("1", width = 120, anchor ='c')
arbol.column("2", width = 120, anchor ='c')
arbol.column("3", width = 180, anchor ='c')

arbol.heading("1", text ="Sesión")
arbol.heading("2", text ="Fecha")
arbol.heading("3", text ="S.O.")

cursor.execute('SELECT * FROM bitacora')
conjunto=cursor.fetchall()

for dt in conjunto: 
    arbol.insert("", 'end', text=dt[0], values=(dt[0],dt[1],dt[2]))


#botoninicia=Button(text="Leer",width=10,command=leerdatos).pack()

raiz.mainloop()