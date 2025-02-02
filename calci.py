from tkinter import *

root = Tk()

root.title("Simple Calculator")

root.geometry("570x600")

root.resizable(False,False)

root.config(bg="white")



equation = ""



def show(value):

    global equation

    equation+=value

    label_res.config(text=equation)



def clear():

    global equation

    equation = ""

    label_res.config(text=equation)



def cal():

    global equation

    result=""

    if equation !="":

        try:

            result =eval(equation)

        except:

            result = "Error"

            equation=""

        label_res.config(text=result)



label_res = Label(root,width=25,height=2,text="",font=("times new roman",30),bg="grey")

label_res.pack()



b1= Button(root,text="C",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear())

b1 .place(x=10,y=100)

b2=Button(root,text="/",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/"))

b2.place(x=150,y=100)

b3=Button(root,text="%",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%"))

b3.place(x=290,y=100)

b4=Button(root,text="x",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*"))

b4.place(x=430,y=100)



b5=Button(root,text="9",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9"))

b5.place(x=10,y=200)

b6=Button(root,text="8",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8"))

b6.place(x=150,y=200)

b7=Button(root,text="7",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7"))

b7.place(x=290,y=200)

b8=Button(root,text="-",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-"))

b8.place(x=430,y=200)



b9=Button(root,text="6",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6"))

b9.place(x=10,y=300)

b10=Button(root,text="5",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5"))

b10.place(x=150,y=300)

b11=Button(root,text="4",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4"))

b11.place(x=290,y=300)

b12=Button(root,text="+",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+"))

b12.place(x=430,y=300)



b13=Button(root,text="3",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3"))

b13.place(x=10,y=400)

b14=Button(root,text="2",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2"))

b14.place(x=150,y=400)

b15=Button(root,text="1",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1"))

b15.place(x=290,y=400)



b16=Button(root,text="0",width=11,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0"))

b16.place(x=10,y=500)

b17=Button(root,text=".",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("."))

b17.place(x=290,y=500)

b18=Button(root,text="=",width=5,height=3,font=("times new roman",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:cal())

b18.place(x=430,y=400)



root.mainloop()

