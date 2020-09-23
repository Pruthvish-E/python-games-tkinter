from tkinter import *
import tkinter.messagebox as msg
'''1    2    
                print(" 1    1)| T |")
                print(" 4)  C    O | I  |2 N |")
                print(" 3     |  M |    |  E |             |3 s |")
                print("4      |  O |    |5 H | E  |  R | O |  I |  N | E  |")                       """e11=e42,e44=e21,e23=e51,e55=e32,e34=e64"""
                print(" 5     |  R |    |  A |             |  l |")
                print(" 6     |  R |         |6 E | N  | V |  E |  L | O  | P  |  E |")
                print(" 7     |  O |                       |  N |")
                print(" 8     |  W |                       |  C |")
                print("  9                                |  E |")'''
'''def click():                                                                                                                            
        s1=e1.get()[0]
        s2=e2.get()[0]
        s3=e3.get()[0]
        s4=e4.get()[0]
        str1=s1+s2+s3+s4
        if str1=="coin" or str1=="COIN":
            print("horray")
        else:
            print("incorrect")'''
        
        
c=Tk()
c.title("CROSSWORD OF RIDDLES")
c.configure(background="blue")
Label(c,text="COMPLETE THE CROSSWORD:",bg="black",fg="white",font="none 12 bold").grid(row=0,columnspan=23)
"""l1=Label(c,text="1)",fg="red")
l1.grid(row=2,column=8,columnspan=2)
e1=Entry(c,width=1,bg="white")
e1.grid(row=2,column=10)
e2=Entry(c,width=1,bg="white")
e2.grid(row=2,column=11)
e3=Entry(c,width=1,bg="white")
e3.grid(row=2,column=12)
e4=Entry(c,width=1,bg="white")
e4.grid(row=2,column=13)
submit=Button(c,text="SUBMIT",command=click)
submit.grid(row=4,columnspan=6)"""
Label(c,text="\n\n",bg="blue",fg="blue").grid(row=1,rowspan=2)
#tomorrow
Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e11=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e11.grid(row=2,column=9,columnspan=2,rowspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e12=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e12.grid(row=3,column=9,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e13=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e13.grid(row=4,column=9,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e14=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e14.grid(row=5,column=9,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e15=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e15.grid(row=6,column=9,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e16=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e16.grid(row=7,column=9,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e17=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e17.grid(row=8,column=9,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e18=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e18.grid(row=9,column=9,columnspan=2)
#coin
Label(c,text="4)",fg="red").grid(row=3,column=4,columnspan=2)
e41=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e41.grid(row=3,column=7,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e43=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e43.grid(row=3,column=11,columnspan=2)
#Label(c,text="1)",fg="red").grid(row=2,column=7,columnspan=2)
e44=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e44.grid(row=3,column=13,columnspan=2)
#neha
Label(c,text="2)",fg="red").grid(row=2,column=13,columnspan=2)
e22=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e22.grid(row=4,column=13,columnspan=2)
e23=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e23.grid(row=5,column=13,columnspan=2)
e24=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e24.grid(row=6,column=13,columnspan=2)

#5heroine

Label(c,text="5)",fg="red").grid(row=5,column=11,columnspan=2)
e52=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e52.grid(row=5,column=15,columnspan=2)
e53=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e53.grid(row=5,column=17,columnspan=2)
e54=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e54.grid(row=5,column=19,columnspan=2)
e55=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e55.grid(row=5,column=21,columnspan=2)
e56=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e56.grid(row=5,column=23,columnspan=2)
e57=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e57.grid(row=5,column=25,columnspan=2)
#3silence
Label(c,text="3)",fg="red").grid(row=3,column=21,columnspan=2)
e31=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e31.grid(row=4,column=21,columnspan=2)
e33=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e33.grid(row=6,column=21,columnspan=2)
e34=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e34.grid(row=7,column=21,columnspan=2)
e35=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e35.grid(row=8,column=21,columnspan=2)
e36=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e36.grid(row=9,column=21,columnspan=2)
e37=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e37.grid(row=10,column=21,columnspan=2)
#6envelope
Label(c,text="6)",fg="red").grid(row=7,column=13,columnspan=2)
e61=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e61.grid(row=7,column=15,columnspan=2)
e62=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e62.grid(row=7,column=17,columnspan=2)
e63=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e63.grid(row=7,column=19,columnspan=2)
e65=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e65.grid(row=7,column=23,columnspan=2)
e66=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e66.grid(row=7,column=25,columnspan=2)
e67=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e67.grid(row=7,column=27,columnspan=2)
e68=Entry(c,width=2,bg="white",fg="green",font="none 12 bold")
e68.grid(row=7,column=29,columnspan=2)
e42=e12
e21=e44
e51=e23
e32=e55
e64=e34
def check():
    global score
    score=0
    #tomorrow
    try:
        s11=e11.get()[0]
        s12=e12.get()[0]
        s13=e13.get()[0]
        s14=e14.get()[0]
        s15=e15.get()[0]
        s16=e16.get()[0]
        s17=e17.get()[0]
        s18=e18.get()[0]
        ans1=s11+s12+s13+s14+s15+s16+s17+s18
        if ans1=="tomorrow" or ans1=="TOMORROW":
            score+=100
    #neha
        s21=e21.get()[0]
        s22=e22.get()[0]
        s23=e23.get()[0]
        s24=e24.get()[0]
        ans2=s21+s22+s23+s24
        if ans2=="neha" or ans2=="NEHA":
            score+=100
    #silence
        s31=e31.get()[0]
        s32=e32.get()[0]
        s33=e33.get()[0]
        s34=e34.get()[0]
        s35=e35.get()[0]
        s36=e36.get()[0]
        s37=e37.get()[0]
        ans3=s31+s32+s33+s34+s35+s36+s37
        if ans3=="silence" or ans3=="SILENCE":
            score+=100
    #coin
        s41=e41.get()[0]
        s42=e42.get()[0]
        s43=e43.get()[0]
        s44=e44.get()[0]
    #s35=e35.get()[0]

    #s36=e36.get()[0]
    #s37=e37.get()[0]
        ans4=s41+s42+s43+s44
        if ans4=="coin" or ans4=="COIN":
            score+=100
    #heroine
        s51=e51.get()[0]
        s52=e52.get()[0]
        s53=e53.get()[0]
        s54=e54.get()[0]
        s55=e55.get()[0]
        s56=e56.get()[0]
        s57=e57.get()[0]
        ans5=s51+s52+s53+s54+s55+s56+s57
        if ans5=="heroine" or ans5=="HEROINE":
            score+=100
    #envelope
        s61=e61.get()[0]
        s62=e62.get()[0]
        s63=e63.get()[0]
        s64=e64.get()[0]
        s65=e65.get()[0]
        s66=e66.get()[0]
        s67=e67.get()[0]
        s68=e68.get()[0]
        ans6=s61+s62+s63+s64+s65+s66+s67+s68
        if ans6=="envelope" or ans6=="ENVELOPE":
            score+=100
        
        msg.showinfo("YOUR SCORE",score)
    except:
        msg.showinfo("ALERT","DONT LEAVE BLANCK SPACES")
#imag=PhotoImage(file="riddle.gif")
#Label(c,image=imag).grid(row=15,columnspan=200,rowspan=200)

questions=Label(c,text=''' DOWN :\n
        \t 1) I am always coming but sadly never arriving\n
        \t2) Neha's father as three children june,july, what is the name of the third child\n
        \t3) What is that you break even when you name it\n
        \n
        
         ACROSS :\n
        
        \t4) What as only a head and a tail and you use it everyday\n
        \t5) The first 2 letters are of a man,first 3 are female,first 4 is greatman or heroic,whole word is a heroic female, what is the full word\n
        \t6) what starts with a E ends with a E and contains one letter in it\n''',bg="pink",fg="black",font="none 12 bold")
questions.grid(row=17,rowspan=18,columnspan=200,sticky=W)
Button(c,text="submit",command=check).grid(row=16,column=30,columnspan=10)
def exit_window():
    c.destroy()
    exit()
Button(c,text="EXIT",command=exit_window,fg="red").grid(row=36,column=80,columnspan=8)

c.mainloop()
