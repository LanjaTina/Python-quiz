#coding:utf-8

import json
import tkinter
from tkinter import *
import random


with open('./question.json', encoding="utf8") as f:
    data = json.load(f)

# convertit le disctionnaire en questions et réponses
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,2,3,1,0,2,1,1,0,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 10):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    print(score)
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#fff",
        foreground="#000",
        border = 0,
    )
    labelimage.pack(pady=(50,50))
    labelresulttext = Label(
        root,
        font = ("Consolas",15),
        background = "#fff",
        foreground="#000",
    )
    labelresulttext.pack()
    nom = Entry
    if (score > 70 and score >= 100):
        img = PhotoImage(file="assets/bravo.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Félicitation!!\nVotre score  est de:{} %".format(str(score)))
        Button(root, image = img3,relief = FLAT,border = 0,command=quit).pack() 
    elif (score > 40 and score <= 70):
        img = PhotoImage(file="assets/ok-removebg-preview.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Bravo!!\nVotre score  est de:{} %".format(str(score)))
        Button(root, image = img3,relief = FLAT,border = 0,command=quit).pack()
    else:
        img = PhotoImage(file="assets/bad-removebg-preview.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Merci d'avoir participer!\nVotre score  est de:{} %".format(str(score)))
        Button(root, image = img3,relief = FLAT,border = 0,command=quit).pack()

def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 10
        x += 1
    #print(score)
    showresult(score)
    return score
ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 30, "bold"),
        width = 500,
        justify = "center",
        wraplength = 1000,
        background = "#fff",
        foreground="#188458",
    )
    lblQuestion.pack(pady=(150,150))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 20),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#fff",
        foreground="black",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 20),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#fff",
        foreground="black",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 20),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#fff",
        foreground="black",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 20),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#fff",
        foreground="black",
    )
    r4.pack(pady=5)

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()

#création de la fenetre
root = tkinter.Tk()
root.title("Virtual recrutment")
root.attributes('-fullscreen', True)
root.config(background="#fff")
#.resizable(0,0) #pour ne pas agrandir le fenetre
img1 = PhotoImage(file="assets/virtual recrutment (3).png")


labelimage = Label(
    root,
    image = img1,
    background = "#fff",
)
labelimage.pack(pady=(50,25))

labeltext = Label(
    root,
    text = "Bienvenue sur notre Quiz de recrutement",
    font = ("Comic sans MS",24,"bold"),
    background = "#fff",
    foreground= "#3CB371"
)
labeltext.pack(pady=(10,50))

img2 = PhotoImage(file="assets/Frame.png")
img3 = PhotoImage(file="assets/quit.png")

lblInstruction = Label(
    root,
    text = "Veuillez bien lire les consignes ci-dessous avant de commencer!",
    background = "#fff",
    foreground= "black",
    font = ("Consolas",18,"bold"),
    justify = "center",
)
lblInstruction.pack(pady=(10,10))


lblRules = Label(
    root,
    text = "I.Vous Disposez de 5 minutes pour répondre aux 10 questions\n\n II.Lorsque vous choisissez une réponse, vous ne pouvez plus révenir à la question précedente\n\n III.ATTENTION!!! vous ne pouvez pas quitter le quiz sinon vous êtes disqualifiés",
    width = 100,
    font = ("Times",16,"bold"),
    background = "#fff",
    foreground = "red",
)
lblRules.pack(pady=(50,50))

btnStart = Button(
    root,
    image = img2,
    relief = RAISED,
    border = 0,
    command = startIspressed,
    background="#fff"
)
btnStart.pack()


root.mainloop()