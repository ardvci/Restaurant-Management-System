#Importing Libraries
from tkinter import*
import random
import time
  
root=Tk()
root.geometry("1600x800+0+0")
root.title("restaurant example")
  
rand=StringVar()
fries=StringVar()
burger=StringVar()
fileto=StringVar()
chicken=StringVar()
cheese=StringVar()
drinks=StringVar()
costofmeal=StringVar()
servicecharge=StringVar()
statetax=StringVar()
subtotal=StringVar()
totalcost=StringVar()
 
text_input=StringVar()
operator=""
#===========================================Body Parts of the GUI=======================================================================================
Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)
  
f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
  
f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
  
localtime=time.asctime(time.localtime(time.time()))
  
lblinfo=Label(Tops,font=('arial',50,'bold'),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
  
lblinfo=Label(Tops,font=('arial',30,'bold'),text=localtime,fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=1,column=0)
#===============================Functions for the buttons===================================================================== 
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
  
def btncleardisplay():
    global operator
    operator=""
    text_input.set("")
  
def btnequals():
    global operator
    semup=str(eval(operator))
    text_input.set(semup)
    operator=""
  
def btonreset():
    rand.set("")
    fries.set("")
    chicken.set("")
    cheese.set("")
    drinks.set("")
    costofmeal.set("")
    servicecharge.set("")
    statetax.set("")
    subtotal.set("")
    totalcost.set("")
    fileto.set("")
    burger.set("")
#================================================I use random numbers for the referance of the order as soon as I learn SQL I will add this data from the database that I create========== 
#I also make the calculations of the order in this funciton=============================================================================================================
def referance():
    x=random.randint(10000,50000)
    randomref=str(x)
    rand.set(randomref)
    Cof=float(fries.get())
    Cod=float(drinks.get())
    Cofile=float(fileto.get())
    Coburger=float(burger.get())
    ccburger=float(chicken.get())
    cheese_burger=float(cheese.get())

    cost_of_fries=Cof*0.99
    cost_of_drinks=Cod*1.0
    cost_of_file=Cofile*2.99
    cost_of_burger=Coburger*3.0
    cost_of_chicken_burger=ccburger*2.5
    cost_of_cheese_burger=cheese_burger*2.7

    cost_of_meal="$",str('%.2f'%(cost_of_fries+cost_of_drinks+cost_of_file+cost_of_burger+cost_of_chicken_burger+cost_of_cheese_burger))
    tax=((cost_of_fries+cost_of_drinks+cost_of_file+cost_of_burger+cost_of_chicken_burger+cost_of_cheese_burger)*0.2)
    Total_cost=(cost_of_fries+cost_of_drinks+cost_of_file+cost_of_burger+cost_of_chicken_burger+cost_of_cheese_burger)
    Ser_charge=((cost_of_fries+cost_of_drinks+cost_of_file+cost_of_burger+cost_of_chicken_burger+cost_of_cheese_burger)/99)
    service="$",str('%2.f'%Ser_charge)
    overallcost="$",str("%2.f"%(tax+Total_cost+Ser_charge))
    paidtax="$",str("%2.f"%tax)
    servicecharge.set(service)
    costofmeal.set(cost_of_meal)
    statetax.set(paidtax)
    subtotal.set(cost_of_meal)
    totalcost.set(overallcost)
  
def btnexit():
    root.destroy()
 
txtDisplay=Entry(f2,font=('arial',30,'bold'),textvariable=text_input,bg="powder blue",bd=30,insertwidth=4,justify="left")
  
txtDisplay.grid(columnspan=4)
#================================================================Calculator Buttons===============================================================================
bton1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",bg="powder blue",anchor='w',command=lambda: btnClick(1)).grid(row=2,column=0)
bton2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=2,column=1)
bton3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=2,column=2)
bton4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)
bton5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)
bton6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)
bton7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=4,column=0)
bton8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=4,column=1)
bton9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=4,column=2)
bton0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=1)
#=================================================================================================================================================
btonclr=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",bg="powder blue",command=btncleardisplay).grid(row=5,column=0)
btonEQL=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",bg="powder blue",command=btnequals).grid(row=5,column=2)
#==================================================================================================================================================
add=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)
subs=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)
multi=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)
div=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)
  
#==================================================================Label of the Entries=======================================================================================
  
lblReference=Label(f1,font=("arial",16,"bold"),text="reference",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=("arial",16,"bold"),textvariable=rand,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtReference.grid(row=0,column=1)
  
lblfries=Label(f1,font=("arial",16,"bold"),text="fries",bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=("arial",16,"bold"),textvariable=fries,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtfries.grid(row=1,column=1) 
  
lblburger=Label(f1,font=("arial",16,"bold"),text="burger",bd=16,anchor='w')
lblburger.grid(row=2,column=0)
txtburger=Entry(f1,font=("arial",16,"bold"),textvariable=burger,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtburger.grid(row=2,column=1) 
  
lblfileto=Label(f1,font=("arial",16,"bold"),text="fileto",bd=16,anchor='w')
lblfileto.grid(row=3,column=0)
txtfileto=Entry(f1,font=("arial",16,"bold"),textvariable=fileto,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtfileto.grid(row=3,column=1) 
  
lblchicken=Label(f1,font=("arial",16,"bold"),text="chicken",bd=16,anchor='w')
lblchicken.grid(row=4,column=0)
txtchicken=Entry(f1,font=("arial",16,"bold"),textvariable=chicken,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtchicken.grid(row=4,column=1) 
  
lblcheese=Label(f1,font=("arial",16,"bold"),text="cheese",bd=16,anchor='w')
lblcheese.grid(row=5,column=0)
txtcheese=Entry(f1,font=("arial",16,"bold"),textvariable=cheese,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtcheese.grid(row=5,column=1) 
  
#======================================================================================================================================
  
lbldrinks=Label(f1,font=("arial",16,"bold"),text="drinks",bd=16,anchor='w')
lbldrinks.grid(row=0,column=3)
txtdrinks=Entry(f1,font=("arial",16,"bold"),textvariable=drinks,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtdrinks.grid(row=0,column=4)
  
  
lblcostofmeal=Label(f1,font=("arial",16,"bold"),text="costofmeal",bd=16,anchor='w')
lblcostofmeal.grid(row=1,column=3)
txtcostofmeal=Entry(f1,font=("arial",16,"bold"),textvariable=costofmeal,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtcostofmeal.grid(row=1,column=4) 
  
lblservisecharge=Label(f1,font=("arial",16,"bold"),text="servicecharge",bd=16,anchor='w')
lblservisecharge.grid(row=2,column=3)
txtservisecharge=Entry(f1,font=("arial",16,"bold"),textvariable=servicecharge,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtservisecharge.grid(row=2,column=4) 
  
lblstatetax=Label(f1,font=("arial",16,"bold"),text="statetax",bd=16,anchor='w')
lblstatetax.grid(row=3,column=3)
txtstatetax=Entry(f1,font=("arial",16,"bold"),textvariable=statetax,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtstatetax.grid(row=3,column=4) 
  
lblsubtotal=Label(f1,font=("arial",16,"bold"),text="subtotal",bd=16,anchor='w')
lblsubtotal.grid(row=4,column=3)
txtsubtotal=Entry(f1,font=("arial",16,"bold"),textvariable=subtotal,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txtsubtotal.grid(row=4,column=4) 
  
lbltotalcost=Label(f1,font=("arial",16,"bold"),text="totalcost",bd=16,anchor='w')
lbltotalcost.grid(row=5,column=3)
txttotalcost=Entry(f1,font=("arial",16,"bold"),textvariable=totalcost,bd=16,insertwidth=4,
    bg="powder blue",justify='left')
txttotalcost.grid(row=5,column=4) 
#==========================================Main Buttons==================================================================
  
btnreset=Button(f1,padx=35,pady=12,bd=10,fg="black",font=("arial",20,"bold"),text="reset",bg="powder blue",command=btonreset)
btntotal=Button(f1,padx=35,pady=12,bd=10,fg="black",font=("arial",20,"bold"),text="total",bg="powder blue",command=referance)
 
btnexit=Button(f1,padx=35,pady=12,bd=10,fg="black",font=("arial",20,"bold"),text="exit",bg="powder blue",command=btnexit)
 
btnreset.grid(row=8,column=1)
btnexit.grid(row=8,column=3)
btntotal.grid(row=8,column=0)
 
 
root.mainloop()
