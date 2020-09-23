from tkinter import *
def exit_window():
        gameover.destroy()
        operator.destroy()
        exit()
def gameoverfn():
        global gameover
        gameover=Tk() 
        gameover.title("GAME OVER")
        Label(gameover,text="GAME OVER",fg="RED",bg="black",font="none 40 bold",width=30).grid(columnspan=30)
        b1=Button(gameover,text="QUIT",command=exit_window)
        b2=Button(gameover,text="TRY AGAIN",command=gameover.destroy)
        b1.grid(row=1,column=12)
        b2.grid(row=1,column=16)
        gameover.mainloop()
def gameoverfn1():
        global gameover
        gameover=Tk()
        gameover.title("WELL DONE")
        Label(gameover,text="CONGRATULATIONS BRAINIAC",fg="RED",bg="black",font="none 40 bold",width=30).grid()
        b1=Button(gameover,text="EXIT",command=exit_window)
        b1.grid(row=1)
        gameover.mainloop()
        operator.destroy()
#def sucess2():
#       sucess=Tk()
#       sucess.title("WELL DONE")
#       Label(sucess,text="WELL DONE BRAINIAC",bg="pink",fg="black",font="none 40 bold",widht=30).grid()
#       b2=Button(sucess,text="EXIT",command=exit_window2)
#       b2.grid(row=1)
#       sucess.mainloop()
        
def operatorgame():
        global operator
        operator=Tk()
        operator.title("OPERATOR GAME")
        operatorimage=PhotoImage(file="operation.gif")
        Label(operator,image=operatorimage).grid(row=0,column=0)
#frame=Frame(operator).grid(row=1)
        l1=Label(operator,text="choose the correct operator + - * / and complete the expression",bg="pink",fg="black",font="none 12 bold")
        l1.grid(row=1)

#button functions
        #operator.destroy()
        #exit()

        Label(operator,text="3__5__10__24__1 = 2",fg="blue",font="none 16 bold").grid(row=2,column=0)
#options
        Label(operator,text="OPTIONS-",fg="green").grid(row=3)
        b1=Button(operator,text="1) +  -  -  *",fg="black",width=12,font="none 12 bold",command=gameoverfn)
        b1.grid(row=4,column=0)
        b2=Button(operator,text="2) +  /  -  *",fg="black",width=12,font="none 12 bold",command=gameoverfn)
        b2.grid(row=5,column=0)
        b3=Button(operator,text="3) *  +  -  +",fg="black",width=12,font="none 12 bold",command=gameoverfn1)
        b3.grid(row=6,column=0)
        b4=Button(operator,text="4) +  -  -  /",fg="black",width=12,font="none 12 bold",command=gameoverfn)
        b4.grid(row=7,column=0)
        operator.mainloop()
operatorgame()
