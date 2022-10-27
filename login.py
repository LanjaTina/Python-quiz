#coding:utf-8

from tkinter import*
from tkinter import messagebox
import tkinter.messagebox as msg
import os
import random

from pkg_resources import EntryPoint
from pyparsing import NoMatch


root = Tk()
root.attributes('-fullscreen', True)
root.title('Quiz')

my_menu = Menu(root)
root.config(menu=my_menu)
photo=PhotoImage(file="assets/Quiz-Logo-PNG-HD-removebg-preview.png")
lb=Label(root, image=photo)
lb.place(x=600, y=30)
photo1=PhotoImage(file="assets/maxresdefault-removebg-preview-removebg-preview.png")
lb1=Label(root, image=photo1)
lb1.place(x=55, y=500)
photo2=PhotoImage(file="assets/4738813-middle-removebg-preview.png")
lb2=Label(root, image=photo2)
lb2.place(x=30, y=200)
label1=Label(root, text='Nom:', font=('Georgia', 30))
label1.place(x=300, y=150)
label2=Label(root, text='Prénom:', font=('Georgia', 30))
label2.place(x=300, y=250)
label3=Label(root, text='Age:', font=('Georgia', 30))
label3.place(x=300, y=350)
label4=Label(root, text='Numéro:', font=('Georgia', 30))
label4.place(x=300, y=450)
entry1= Entry(root, font=('Georgia', 30), background="#f0e68c")
entry1.place(x=500, y=150)
entry2= Entry(root, font=('Georgia', 30), background="#f0e68c" )
entry2.place(x=500, y=250)
entry3= Entry(root, font=('Georgia', 30), background="#f0e68c")
entry3.place(x=500, y=350)
entry4= Entry(root, font=('Georgia', 30), background="#f0e68c")
entry4.place(x=500, y=450)
    
def quiz():
    root.destroy()        
    fileToOpen = r"C:\Users\Finoana\Desktop\Projet 11\Groupe 11 PROJET 12\Virtual recrutment projet\quiz_esti.py"
    os.system("python {}".format(fileToOpen))
    
button1=Button(root, text="Suivant", font=('Georgia', 30), bg='dark orange', command= quiz)
button1.place(x=600, y= 550)

root.mainloop()
