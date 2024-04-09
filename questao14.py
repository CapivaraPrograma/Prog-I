from tkinter import *
from tkinter import messagebox

def login():
    
root = Tk()
root.configure(bg="cyan4")

label1 = Label(root, text='Login', bg="cyan4", fg="cyan", font=("Arial",20))
label1.place(x=500, y=20)

label2 = Label(root, text="Nome de Usuario: ", font=("Areal",20), bg="cyan4", fg="white")
label2.place(x=310, y=190)

label3 = Label(root, text="Senha do Usuario: ", font=("Areal",20), bg="cyan4", fg="white")
label3.place(x=310, y=340)

entry1 = Entry(root,font=("Areal",20))
entry1.place(x=600, y=200)

entry2 = Entry(root,font=("Areal",20), show="*")
entry2.place(x=600, y=350)

button = Button(root, text="Login", bg="cyan3", font=("Areal",15), bd=5)
button.place(x=600,y=500)
root.mainloop()