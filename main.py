import tkinter
from tkinter import *
import tkinter.messagebox
import datetime
import csv
import os
from Classes import Corns
from Classes import Classic
from Classes import Goat_cheese
from Classes import Margherita
from Classes import Plain
from Classes import Turkish
from Classes import Meat
from Classes import Mushrooms
from Classes import Olives
from Classes import Onions


root = Tk()
root.geometry("800x600")
root.title("Pizza Ordering System")

logo = PhotoImage(file="pizza_logo.png")
photoLabel = Label(root, image=logo)
photoLabel.place(x=0, y=5)

banner = PhotoImage(file="pizza_banner.png")
photoBanner = Label(root, image=banner)
photoBanner.place(x=100, y=0)

v = tkinter.StringVar()
total_cost=0
order_details=[]
c1=IntVar()
c2=IntVar()
c3=IntVar()
c4=IntVar()
c5=IntVar()
c6=IntVar()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
isSelected=0
calculatedCost=0

def cost_calc():
    global total_cost
    global order_details
    global isSelected
    if v.get()=='1':
        cl = Classic()
        total_cost += cl.get_cost()
        order_details.append("Classic")
        isSelected=1

    elif v.get()=='2':

        ma = Margherita()
        total_cost += ma.get_cost()
        order_details.append("Margherita")
        isSelected=1

    elif v.get() == '3':

        tr = Turkish()
        total_cost += tr.get_cost()
        order_details.append("Turkish")
        isSelected=1


    elif v.get() == '4':

        pl = Plain()
        total_cost += pl.get_cost()
        order_details.append("Plain")
        isSelected=1


    else:
        isSelected=0

    if c1.get()==1:
        ol = Olives()
        total_cost += ol.get_cost()
        order_details.append("Olives")
    if c2.get()==1:
        mu = Mushrooms()
        total_cost += mu.get_cost()
        order_details.append("Mushrooms")
    if c3.get()==1:
        g = Goat_cheese()
        total_cost += g.get_cost()
        order_details.append("Goat Cheese")
    if c4.get()==1:
        m = Meat()
        total_cost += m.get_cost()
        order_details.append("Meat")
    if c5.get()==1:
        o = Onions()
        total_cost += o.get_cost()
        order_details.append("Onions")
    if c6.get()==1:
        c = Corns()
        total_cost += c.get_cost()
        order_details.append("Corns")


lblCost=Label(root,text="Total Cost: 0$",font=('Arial', 10, "bold"),bg="orange")
lblCost.place(x=480,y=513)

def displayCost():
    global calculatedCost
    isChecked=0
    if v.get()=='1':
        calculatedCost=0
        cl = Classic()
        calculatedCost += cl.get_cost()
        isChecked = 1

    elif v.get()=='2':
        calculatedCost = 0
        ma = Margherita()
        calculatedCost += ma.get_cost()
        isChecked = 1

    elif v.get() == '3':
        calculatedCost = 0
        tr = Turkish()
        calculatedCost += tr.get_cost()
        isChecked = 1

    elif v.get() == '4':
        calculatedCost = 0
        pl = Plain()
        calculatedCost += pl.get_cost()
        isChecked = 1

    else:
        calculatedCost+=0
        isChecked = 0

    if c1.get()==1:
        if isChecked==0:
            tkinter.messagebox.showwarning("","Please choose a pizza")
            c1.set(0)
        else:
            ol = Olives()
            calculatedCost += ol.get_cost()

    if c2.get()==1:
        if isChecked==0:
            tkinter.messagebox.showwarning("", "Please choose a pizza")
            c2.set(0)
        else:
            mu = Mushrooms()
            calculatedCost += mu.get_cost()

    if c3.get()==1:
        if isChecked==0:
            tkinter.messagebox.showwarning("", "Please choose a pizza")
            c3.set(0)
        else:
            g = Goat_cheese()
            calculatedCost += g.get_cost()

    if c4.get()==1:
        if isChecked==0:
            tkinter.messagebox.showwarning("", "Please choose a pizza")
            c4.set(0)
        else:
            m = Meat()
            calculatedCost += m.get_cost()

    if c5.get()==1:
        if isChecked==0:
            tkinter.messagebox.showwarning("", "Please choose a pizza")
            c5.set(0)
        else:
            o = Onions()
            calculatedCost += o.get_cost()

    if c6.get()==1:
        if isChecked==0:
            tkinter.messagebox.showwarning("", "Please choose a pizza")
            c5.set(0)
        else:
            c = Corns()
            calculatedCost += c.get_cost()

    strCost="Total Cost: "+str(calculatedCost)+"$"
    lblCost.config(text=strCost)

def onClick():
    global isSelected

    if var1.get()=="":
        tkinter.messagebox.showinfo("Order information", "Please enter your name and surname correctly")
    elif var2.get()=="":
        tkinter.messagebox.showinfo("Order information", "Please enter your social security number correctly")
    elif var3.get()== "":
        tkinter.messagebox.showinfo("Order information", "Please enter your credit card number correctly")
    elif var4.get()=="":
        tkinter.messagebox.showinfo("Order information", "Please enter your credit card password correctly")
    else:
        if isSelected == 1:
            write()
            tkinter.messagebox.showinfo("Order information", "Order is placed")
        elif isSelected == 0:
            tkinter.messagebox.showinfo("Order information", "Please select a pizza")
        else:
            tkinter.messagebox.showinfo("Order information", "Program Error")


label1 = Label(root, text="MENU", font=('Arial', 15, 'bold'))
label1.place(x=200, y=110)
margarita = PhotoImage(file="margarita.png")
photoLabel2 = Label(root, image=margarita)
photoLabel2.place(x=20, y=250)
ingredients2 = Label(root, text="Margherita Pizza", font=('Arial', 11, 'bold'), fg="orange")
ingredients2.place(x=130, y=250)
ingredientsList2 = Label(root,
                         text="Fragrant basil, velvety mozzarella, and herb-infused\n tomato sauce come together on a crispy crust to\n transport you to the hills of Italy with each flavorful bite.",
                         font=('Arial', 8, 'bold'), fg="gray")
ingredientsList2.place(x=130, y=270)
price2 = Radiobutton(root, text="PRICE: 15$", font=('Arial', 10, 'bold'), fg="gray", value=2, variable=v,command=displayCost)
price2.place(x=330, y=320)

plain = PhotoImage(file="plain.png")
photoLabel3 = Label(root, image=plain)
photoLabel3.place(x=20, y=450)
ingredients4 = Label(root, text="Plain Pizza", font=('Arial', 11, 'bold'), fg="orange")
ingredients4.place(x=130, y=450)
ingredientsList4 = Label(root,
                         text="A timeless classic that celebrates high-quality\n ingredients with a crispy crust, luscious tomato sauce, and \na perfect blend of mozzarella and Parmesan cheeses",
                         font=('Arial', 8, 'bold'), fg="gray")
ingredientsList4.place(x=130, y=470)
price4 = Radiobutton(root, text="PRICE: 16$", font=('Arial', 10, 'bold'), fg="gray", value=4,variable=v,command=displayCost)
price4.place(x=330, y=520)

turkish = PhotoImage(file="turkish.png")
photoLabel4 = Label(root, image=turkish)
photoLabel4.place(x=20, y=350)
ingredients3 = Label(root, text="Turkish Pizza", font=('Arial', 11, 'bold'), fg="orange")
ingredients3.place(x=130, y=350)
ingredientsList3 = Label(root,
                         text="A flavorful fusion of Middle Eastern spices, savory\n meats, and fresh veggies on a crispy crust.With a \ncomplex blend of earthy cumin, tangy sumac,and parsley",
                         font=('Arial', 8, 'bold'), fg="gray")
ingredientsList3.place(x=130, y=370)
price3 = Radiobutton(root, text="PRICE: 17$", font=('Arial', 10, 'bold'), fg="gray", value=3,variable=v,command=displayCost)
price3.place(x=330, y=420)

classic = PhotoImage(file="classic.png")
photoLabel5 = Label(root, image=classic)
photoLabel5.place(x=20, y=150)
ingredients1 = Label(root, text="Classic Pizza", font=('Arial', 11, 'bold'), fg="orange")
ingredients1.place(x=130, y=150)
ingredientsList1 = Label(root,
                         text="A perfect blend of crisp crust, tomato sauce and\n savory cheeses. Simple yet flavorful, it's a feast\n for the senses that leaves you craving more",
                         font=('Arial', 8, 'bold'), fg="gray")
ingredientsList1.place(x=130, y=170)
price1 = Radiobutton(root, text="PRICE: 12$", font=('Arial', 10, 'bold'), fg="gray", value=1, variable=v,command=displayCost)
price1.place(x=330, y=220)

label2 = Label(root, text="TOPPINGS", font=('Arial', 15, 'bold'))
label2.place(x=580, y=110)
check1 = Checkbutton(root, text="Olive", font=('Arial', 10, 'bold'), fg="black", variable=c1,onvalue=1,command=displayCost)
check1.place(x=480, y=150)
tprice1 = Label(root, text="PRICE: +1$", font=('Arial', 10, 'bold'), fg="gray")
tprice1.place(x=690, y=150)
check2 = Checkbutton(root, text="Mushroom", font=('Arial', 10, 'bold'), fg="black", variable=c2,onvalue=1,command=displayCost)
check2.place(x=480, y=180)
tprice2 = Label(root, text="PRICE: +1$", font=('Arial', 10, 'bold'), fg="gray")
tprice2.place(x=690, y=180)
check3 = Checkbutton(root, text="Goat Cheese", font=('Arial', 10, 'bold'), fg="black", variable=c3,onvalue=1,command=displayCost)
check3.place(x=480, y=210)
tprice3 = Label(root, text="PRICE: +2$", font=('Arial', 10, 'bold'), fg="gray")
tprice3.place(x=690, y=210)
check4 = Checkbutton(root, text="Meat", font=('Arial', 10, 'bold'), fg="black", variable=c4,onvalue=1,command=displayCost)
check4.place(x=480, y=240)
tprice4 = Label(root, text="PRICE: +2$", font=('Arial', 10, 'bold'), fg="gray")
tprice4.place(x=690, y=240)
check5 = Checkbutton(root, text="Onion", font=('Arial', 10, 'bold'), fg="black", variable=c5,onvalue=1,command=displayCost)
check5.place(x=480, y=270)
tprice5 = Label(root, text="PRICE: +0.5$", font=('Arial', 10, 'bold'), fg="gray")
tprice5.place(x=690, y=270)
check6 = Checkbutton(root, text="Corn", font=('Arial', 10, 'bold'), fg="black", variable=c6,onvalue=1,command=displayCost)
check6.place(x=480, y=300)
tprice6 = Label(root, text="PRICE: +0.5$", font=('Arial', 10, 'bold'), fg="gray")
tprice6.place(x=690, y=300)

label3 = Label(root, text="CUSTOMER INFO", font=('Arial', 15, 'bold'))
label3.place(x=550, y=340)

labelName = Label(root, text="Name Surname", font=('Arial', 10, "bold"))
labelName.place(x=480, y=390)
entryName = Entry(root,textvariable=var1).place(x=650, y=390)



labelSSN = Label(root, text="Social Security Number", font=('Arial', 10, "bold"))
labelSSN.place(x=480, y=420)
entrySSN = Entry(root,textvariable=var2).place(x=650, y=420)

labelCreditCard = Label(root, text="Credit Card Number", font=('Arial', 10, "bold"))
labelCreditCard.place(x=480, y=450)
entryCreditCard = Entry(root,textvariable=var3).place(x=650, y=450)

labelPassword = Label(root, text="Credit Card Password", font=('Arial', 10, "bold"))
labelPassword.place(x=480, y=480)
entryPassword = Entry(root,textvariable=var4).place(x=650, y=480)



buttonPay = Button(root, text="PAY", font=('Arial', 10, "bold"), bg="orange",command=lambda: [cost_calc(),onClick()] )
buttonPay.place(x=735, y=510)



def write():

 with open('Orders_Database.csv','a',newline="")as orders:
    orders= csv.writer(orders,delimiter=',')
    n_s = var1.get()
    ssn = var2.get()
    ccn = var3.get()
    ccp = var4.get()
    time_of_order = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    cost=(f"{total_cost}$")
    if os.stat("Orders_Database.csv").st_size==0:
        orders.writerow(['Name Surname', 'SSN', 'CCN', 'CCP', 'Details', 'Price', 'Date'])
    orders.writerow([n_s,ssn,ccn,ccp,order_details,cost,time_of_order])


root.mainloop()
