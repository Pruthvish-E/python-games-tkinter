from tkinter import *
import tkinter.messagebox as msg
def randomcall():
        global output
        global setpassword 
        setpassword=[]  
        import random
        for i in range(0,5):
                j=random.randint(0,9)
                setpassword.append(j)
                sum=0
        for i in setpassword:
                sum=sum+i
                #print(setpassword)
                #print(sum)
        global listpassword
        listpassword=list(setpassword)
        output.delete(0.0,END)
        s1="hint: sum of numbers is:- "+str(sum)+"\n"
        #hint2=random.randint(0,4)
        s2='Number in which '+str(hint2)+' place is '+str(listpassword[hint2])+' considering starting place to be zeroth place\n'
        s=s1+s2
        output.insert(END,s)
        password()
        
def password():
                #global check
                global userinput
                userinput=entry.get()[:5]
                #print(type(userinput))
                #if len(set(userinput)<4:
                #       print('t enter identical no')
                #       password()
                global check
                check=[]
                for o in userinput:
                    check.append(int(o))
                output.insert(END,str(check))
                passwordcheck()
                    
def passwordcheck():
                global score
                scorestr="PASSWORD CRACKED "+"score-"+str(score)
                global check
                global output
                if len(check)==5:
                        correctno=0
                        position=0
                        for k in range(0,len(check)):
                            if check[k] in listpassword:
                                    correctno+=1
                        for g in range(0,len(check)):
                            if check[g]==listpassword[g]:
                                    position+=1
                        s=set()
                correctpas='no of correct places '+str(position)+'\n'+'no of correct guesses '+str(correctno)+'\n'
                s1="hint: sum of numbers is:- "+str(sum)+"\n"
        #hint2=random.randint(0,4)
                s2='Number in which '+str(hint2)+' place is '+str(listpassword[hint2])+' considering starting place to be zeroth place\n'
                s=s1+s2+correctpas
                if check==listpassword:
                            msg.showinfo('Password Cracked',scorestr)
                            
                    
                
                else:
                    if score==0:
                            msg.showinfo("GAME OVER","GAME OVER")
                            p.destroy()
                    output.delete(0.0,END)
                    output.insert(END,s)
                    msg.showinfo('ALERT','WRONG PASSWORD')
                    
                    
                        #passwordcheck()
                
        





score=1000
p=Tk()
p.title("PASSWORD CRACK")
p.configure(background="pink")
Label(p,text="CRACK THE FIVE (5) DIGIT PASSWORD WITH THE FOLLOWING HINTS:-",fg="red",bg="green",font="none 12 bold").grid(columnspan=60)
def inputuser():
    global score
    global check
    try:
        
        scorestr="PASSWORD CRACKED "+"score-"+str(score) 
        userinput=entry.get()[:5]
        check=[]
        for o in userinput:
            check.append(int(o))
        sc=str(check)+'\n'
        output.delete(0.0,END)
        output.insert(END,sc)
        correctno=0
        position=0 
        for k in range(0,len(check)):
            if check[k] in listpassword:
                correctno+=1
        for g in range(0,len(check)):
            if check[g]==listpassword[g]:
                position+=1
       
        if check==listpassword:
            msg.showinfo("WELL DONE:",scorestr)
            p.destroy()
        else:
           score-=200
           passwordcheck()
    except:
        s2='Number in which '+str(hint2)+' place is '+str(listpassword[hint2])+' considering starting place to be zeroth place\n'
        s=s1+s2
        output.delete(0.0,END)
        output.insert(END,s)
        msg.showinfo("ALERT","ENTER CORRECT FORMAT")
        
           
        
        
        
import random        
        
        

#######
def randompassword():
    global setpassword
    global sum
    setpassword=set()
    
    for i in range(0,5):
        j=random.randint(0,9)
        setpassword.add(j)
    if len(setpassword)==5:
        sum=0
        for i in setpassword:
            sum=sum+i
    else:
        randompassword()
randompassword()
                #print(setpassword)
                #print(sum)
                
listpassword=list(setpassword)
print(listpassword)
s1="hint: sum of numbers is:- "+str(sum)+"\n"
hint2=random.randint(0,4)
s2='Number in which '+str(hint2)+' place is '+str(listpassword[hint2])+' considering starting place to be zeroth place\n'
s=s1+s2
output=Text(p,width=75,height=6,bg="blue",fg="red",font="none 12 bold")
output.grid(row=3,columnspan=75,rowspan=6,sticky=W)
output.insert(END,s)
entry=Entry(p,width=5,fg="black",bg="grey")
entry.grid(row=7,column=4)
b1=Button(p,text="SUBMIT",command=inputuser)
b1.grid(row=10,column=10)
Button(p,text="EXIT",command=p.destroy).grid(row=10,column=14)
p.mainloop()
