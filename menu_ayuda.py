import os
from tkinter import *
from PIL import ImageTk, Image


raiz=Tk()
raiz.title("Menú ayuda")
barramenu=Menu(raiz)
raiz.geometry("950x750")
raiz.resizable(0,0)

frame = Frame(raiz, width=1000, height=300)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("Ayuda_usuario.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

raiz.mainloop()