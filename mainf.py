from tkinter import *
import os
def crossword():
    os.system("crosswordf.py")
    return
def guess():
    os.system("guesspruf.py")
    return
def moon():
    os.system("moonf.py")
    return
def operator():
    os.system("operatorf.py")
    return
def password():
    os.system("p2f.py")
    return
main=Tk()
main.title("BRAINIAC: THE THINKER")
img=PhotoImage(file="riddle.gif")
main.configure(background="black")
Label(main,text="WELCOME TO BRAINIAC:- THE THINKER",fg="red",bg="black",font="none 12 bold").grid(columnspan=33)
Label(main,text="MAIN MENU-",fg="red",bg="blue",font="none 12 bold").grid(row=1,columnspan=10)
Label(main,image=img,width=500,height=500).grid(row=2,column=0,columnspan=500,rowspan=500)
g4=Button(main,text="CROSSWORD",command=crossword)
g3=Button(main,text="GUESS GAME",command=guess)
g2=Button(main,text="COMMON SENSE TEST",command=moon)
g1=Button(main,text="OPERATOR GAME",command=operator)
g5=Button(main,text="PASSWORD CRACK",command=password)
Label(main,text="LEVEL 1:-",fg="red",bg="blue").grid(row=80,column=20)
g1.grid(row=100,column=30)
Label(main,text="LEVEL 2:-",fg="red",bg="blue").grid(row=120,column=20)
g2.grid(row=140,column=30)
Label(main,text="LEVEL 3:-",fg="red",bg="blue").grid(row=160,column=20)
g3.grid(row=180,column=30)
Label(main,text="LEVEL 4:-",fg="red",bg="blue").grid(row=200,column=20)
g4.grid(row=220,column=30)
Label(main,text="LEVEL 5:-",fg="red",bg="blue").grid(row=240,column=20)
g5.grid(row=260,column=30)
main.mainloop()
