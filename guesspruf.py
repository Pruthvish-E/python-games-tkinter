from tkinter import *
import tkinter.messagebox as msg
guess=Tk()
guess.title("GUESS THE NUMBER")
guess.configure(background="black")
def textget():
    global c
    if c<11:
        try:
            e1=int(e.get()[:5])
            if e1==num:
                msg.showinfo("WELL DONE","PERFECT GUESS")
                guess.destroy()
            if e1>num:
                c=c+1
                s1="YOUR GUESS IS HIGH"
                o.delete(0.0,END)
                o.insert(END,s1)
            if e1<num:
                c=c+1
                s2="YOUR GUESS IS LOW"
                o.delete(0.0,END)
                o.insert(END,s2)
        except:
            msg.showinfo("ALERT","PLEASE ENTER ONLY POSITIVE INTEGERS")
    else:
        msg.showinfo("GAME OVER","YOU TOOK MORE THAN 10 ATTEMPTS")
        guess.destroy()
import random
from random import randint as ri
c=0
num=ri(0,1024)
print(num)
Label(guess,text="GUESS THE NUMBER BETWEEN 0 TO 1024",fg="gold",bg="black",font="none 12 bold").grid(columnspan=34)
o=Text(guess,width=20,height=1)
o.grid(row=1)
o.insert(0.0,"GUESS A NUMBER")
e=Entry(guess,fg="red",width=4)
e.grid(row=2)
Button(guess,text="SUBMIT",command=textget).grid(row=3,column=10)
guess.mainloop()
