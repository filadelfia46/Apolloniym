import tkinter
from tkinter import *
from tkinter import messagebox,Canvas
import random
from random import randint

root = Tk()
root.title("Чертеж")
root.configure()

#построение окружности
def chengtext1():
    #cl = ['#5d44a2','#b5319b','#ff9308','#960018','#082567','#990066','#6e7eae']
    coordinates = []
    coordinates.append(int(x1.get()))
    coordinates.append(int(y1.get()))
    coordinates.append(int(rq.get()))
    coordinates.append(int(x2.get()))
    coordinates.append(int(y2.get()))
    coordinates.append(int(rr.get()))
    coordinates.append(int(x3.get()))
    coordinates.append(int(y3.get()))
    coordinates.append(int(rt.get()))
    
    for i in range(0,len(coordinates),3):
        s1 = canvas.create_oval(coordinates[i]+coordinates[i+2], coordinates[i+1]+coordinates[i+2], coordinates[i]-coordinates[i+2],coordinates[i+1]-coordinates[i+2],outline='red',width=2)
        
    co = coordinates
    t = 0
    a = 191970
    for x in range(1,600):
        for y in range(1,600):
            r10 = round(((co[0]-x)**2+(co[1]-y)**2)**0.5)- co[2]
            r20 = round(((co[3]-x)**2+(co[4]-y)**2)**0.5) - co[5]
            r30 = round(((co[6]-x)**2+(co[7]-y)**2)**0.5)-co[8]
            
            r1 = round(((co[0]-x)**2+(co[1]-y)**2)**0.5)+ co[2]
            r2 = round(((co[3]-x)**2+(co[4]-y)**2)**0.5) + co[5]
            r3 = round(((co[6]-x)**2+(co[7]-y)**2)**0.5)+co[8]
            if r1==r2==r3: #or r10==r20==r3 or r10==r2==r3 or r1==r20==r30 or r10==r2==r30 or r1==r20==r3 or r1==r2==r30 or r10==r20==r30:
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if r10==r20==r3:
                r1 = r10
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if r10==r2==r3:
                r1 = r10
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if r1==r20==r30:
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if r10==r2==r30:
                r1 = r10
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if  r1==r20==r3:
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if r1==r2==r30:
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)
                
            if r10==r20==r30:
                r1 = r10
                s1 = canvas.create_oval(x+r1,y+r1,x-r1,y-r1,outline='#'+str(a-t))
                t=random.randint(0,19100)

               









#текст1
b = Label(root, text="Введите координаты окружностей", font=("Arial Bold", 14),fg='#535a53')
b.pack()
#промежуток 1
size = 600
canvas2 = Canvas(root, width=650, height=90)
canvas2.pack()






#поле ввода1
x1 = Entry(root, width=10,bg='#dee5de')
x1.place(x=85,y=50)

b = Label(root, text="x1", font=("Arial Bold", 14),fg='#535a53')
b.place(x=55,y=45)

#поле ввода2
x2 = Entry(root, width=10,bg='#dee5de')
x2.place(x=300,y=50)

b = Label(root, text="x2", font=("Arial Bold", 14),fg='#535a53')
b.place(x=270,y=45)

#поле ввода3
x3 = Entry(root, width=10,bg='#dee5de')
x3.place(x=500,y=50)

b = Label(root, text="x3", font=("Arial Bold", 14),fg='#535a53')
b.place(x=470,y=45)

#поле ввода1
y1 = Entry(root, width=10,bg='#dee5de')
y1.place(x=85,y=75)

b = Label(root, text="y1", font=("Arial Bold", 14),fg='#535a53')
b.place(x=55,y=70)

#поле ввода2
y2 = Entry(root, width=10,bg='#dee5de')
y2.place(x=300,y=75)

b = Label(root, text="y2", font=("Arial Bold", 14),fg='#535a53')
b.place(x=270,y=70)

#поле ввода3
y3 = Entry(root, width=10,bg='#dee5de')
y3.place(x=500,y=75)

b = Label(root, text="y3", font=("Arial Bold", 14),fg='#535a53')
b.place(x=470,y=70)

#поле ввода1
rq = Entry(root, width=10,bg='#dee5de')
rq.place(x=85,y=100)

b = Label(root, text="r1", font=("Arial Bold", 14),fg='#535a53')
b.place(x=55,y=95)

#поле ввода2
rr = Entry(root, width=10,bg='#dee5de')
rr.place(x=300,y=100)

b = Label(root, text="r2", font=("Arial Bold", 14),fg='#535a53')
b.place(x=270,y=95)

#поле ввода3
rt = Entry(root, width=10,bg='#dee5de')
rt.place(x=500,y=100)

b = Label(root, text="r3", font=("Arial Bold", 14),fg='#535a53')
b.place(x=470,y=95)









#промажуток 2
size = 600
canvas = Canvas(root, width=size, height=20)
canvas.pack()


#рабочая поверхность
size = 600
canvas = Canvas(root, width=size, height=size,bg='#dee5de')
canvas.pack()

#система координат
canvas.create_line(0,0,size,0,width=9,fill='#e17576')
canvas.create_line(0,0,0,size,width=9,fill="#3a75c4")
canvas.create_line(size,0,size-15,15,width=5,fill="#e17576")
canvas.create_line(0,size,15,size-15,width=5,fill="#3a75c4")

#кнопка выхода
se = Button(text="выход", font="Arial", fg="#535a53", bg="#c7a5a2",  width=20, command=root.destroy)
se.pack(side=RIGHT)

#кнопка начертить
but = Button(root, text='Начертить',width=20, font=("Arial Bold", 10), command = chengtext1,fg='#535a53',bg='#a5e9c1')
but.pack(side=LEFT)

b = Label(root, text="*Поле 600Х600", font=("Arial Bold", 10),fg='#c7a5a2')
b.pack()

#промежуток 3
size = 600
canvas2 = Canvas(root, width=60, height=30)
canvas2.pack()


root.mainloop()
