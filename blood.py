import tkinter
from tkinter import *
from tkinter import messagebox,Canvas
import random
from random import randint

foregroundColor = "#eee"
backgroundColor = "#555"

root1 = tkinter.Tk()

root1.configure()
root1.title("Касания")


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
            if r1==r2==r3:
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


def osnova():

    #удоление предыдущего поля
    root1.destroy()
    
    root = Tk()
    root.title("Касания")
    root.configure()

    root3 = Tk()
    root3.title("Координаты окружностей")
    root3.configure()
    
    #текст1
    b = Label(root3, text="Введите координаты окружностей", font=("Arial Bold", 14),fg='#535a53')
    b.pack()
    
    #промежуток 1
    size = 600
    canvas2 = Canvas(root3, width=250, height=90)
    canvas2.pack()

    #поле ввода1
    x1 = Entry(root3, width=10,bg='#dee5de')
    x1.place(x=45,y=50)

    b = Label(root3, text="x1", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=15,y=45)

    #поле ввода2
    x2 = Entry(root3, width=10,bg='#dee5de')
    x2.place(x=150,y=50)

    b = Label(root3, text="x2", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=120,y=45)

    #поле ввода3
    x3 = Entry(root3, width=10,bg='#dee5de')
    x3.place(x=255,y=50)

    b = Label(root3, text="x3", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=225,y=45)

    #поле ввода1
    y1 = Entry(root3, width=10,bg='#dee5de')
    y1.place(x=45,y=75)

    b = Label(root3, text="y1", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=15,y=70)

    #поле ввода2
    y2 = Entry(root3, width=10,bg='#dee5de')
    y2.place(x=150,y=75)

    b = Label(root3, text="y2", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=120,y=70)

    #поле ввода3
    y3 = Entry(root3, width=10,bg='#dee5de')
    y3.place(x=255,y=75)

    b = Label(root3, text="y3", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=225,y=70)

    #поле ввода1
    rq = Entry(root3, width=10,bg='#dee5de')
    rq.place(x=45,y=100)

    b = Label(root3, text="r1", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=15,y=95)

    #поле ввода2
    rr = Entry(root3, width=10,bg='#dee5de')
    rr.place(x=150,y=100)

    b = Label(root3, text="r2", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=120,y=95)

    #поле ввода3
    rt = Entry(root3, width=10,bg='#dee5de')
    rt.place(x=255,y=100)

    b = Label(root3, text="r3", font=("Arial Bold", 14),fg='#535a53')
    b.place(x=225,y=95)

    #промажуток 2
    size = 340
    canvas = Canvas(root3, width=size, height=20)
    canvas.pack()

    #рабочая поверхность
    size = 600
    canvas = Canvas(root, width=size, height=size,bg='#dee5de')
    canvas.pack()

    #система координат
    #canvas.create_line(0,0,size,0,width=9,fill='#e17576')
    #canvas.create_line(0,0,0,size,width=9,fill="#3a75c4")
    #canvas.create_line(size,0,size-15,15,width=5,fill="#e17576")
    #canvas.create_line(0,size,15,size-15,width=5,fill="#3a75c4")

    #кнопка выхода
    se = Button(root,text="выход", font="Arial", fg="#535a53", bg="#c7a5a2",  width=20, command=root.destroy)
    se.pack(side=TOP)

    #кнопка начертить
    but = Button(root3, text='Начертить',width=20, font=("Arial Bold", 10), command = chengtext1,fg='#535a53',bg='#a5e9c1')
    but.pack(side=TOP)

    #промежуток 3
    size = 600
    canvas2 = Canvas(root, width=60, height=40)
    canvas2.pack()

    size = 340
    canvas = Canvas(root3, width=size, height=20)
    canvas.pack()

    root.mainloop()
    root3.mainloop()
    
    
def nastoiki():
    #удаление старого поля
    canvas20.destroy()
    but11.destroy()
    b6.destroy()
    b7.destroy()

    #поле настроек
    b73 = Canvas(root1, width=500, height=600,bg='#d6e4ba')
    b73.pack()

    #настройки текст
    b70 = Label(root1, text="Выберите размер поля", font=("@Microsoft YaHei UI Light", 15),fg='#0a0000',bg='#d6e4ba')
    b70.place(x=143,y=14)

    #кнопка далее
    b71 = Button(root1, text='Далее',width=20, font=("@Microsoft YaHei UI Light", 10), command = osnova,fg='#0a0000',bg='#b0d3bf')
    b71.place(x=160,y=490)
    
    #первое поле ввода
    c1 = Entry(root1, width=10,bg='#dee5de')
    c1.place(x=150,y=270)

    #круги над полями ввода
    s1 = b73.create_oval(170,240,190,260,outline="#e17576", fill="#e17576")
    s1 = b73.create_oval(320,240,340,260,outline="#3a75c4", fill="#3a75c4")
    
    #текст на
    b = Label(root1, text="на", font=("@Microsoft YaHei UI Light", 15),fg='#0a0000',bg='#d6e4ba')
    b.place(x=240,y=260)
    
    #второе поле ввода
    c2 = Entry(root1, width=10,bg='#dee5de')
    c2.place(x=297,y=270)

    #слова о размерности
    b = Label(root1, text="*в пикселях", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=220,y=45)

    #рисунок системы координат
    b73.create_line(50,100,450,100,width=7,fill='#e17576')
    b73.create_line(50,97,50,480,width=7,fill='#3a75c4')
    
    b73.create_line(450,100,450-15,100-15,width=5,fill="#e17576")
    b73.create_line(450,100,450-15,100+15,width=5,fill="#e17576")
    b73.create_line(50,480,50-15,480-15,width=5,fill="#3a75c4")
    b73.create_line(50,480,50+15,480-15,width=5,fill="#3a75c4")
    
    #s1 = b73.create_oval(40,110,60,90,outline="#6c4f7e", fill="#6c4f7e")
    
    b73.create_line(150,95,150,107,width=3,fill="#e17576") 
    b73.create_line(250,95,250,107,width=3,fill="#e17576")
    b73.create_line(350,95,350,107,width=3,fill="#e17576")
    
    b73.create_line(42,200,57,200,width=3,fill="#3a75c4")
    b73.create_line(42,300,57,300,width=3,fill="#3a75c4")
    b73.create_line(42,400,57,400,width=3,fill="#3a75c4")

    b = Label(root1, text="100", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=135,y=110)

    b = Label(root1, text="200", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=235,y=110)

    b = Label(root1, text="300", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=335,y=110)
    

    b = Label(root1, text="100", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=60,y=195)

    b = Label(root1, text="200", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=60,y=295)

    b = Label(root1, text="300", font=("@Microsoft YaHei UI Light", 9),fg='#6c6f74',bg='#d6e4ba')
    b.place(x=60,y=395)
    
    
#поле старта
canvas20 = Canvas(root1, width=500, height=600,bg='#d6e4ba')
canvas20.pack()

#кнопка далее
but11 = Button(root1, text='Далее',width=20, font=("@Microsoft YaHei UI Light", 10), command = nastoiki,fg='#0a0000',bg='#b0d3bf')
but11.place(x=160,y=490)

#слова Касании
b6 = Label(root1, text="Я Касания", font=("@Microsoft YaHei UI Light", 15),fg='#0a0000',bg='#d6e4ba')
b6.place(x=200,y=10)
b7 = Label(root1, text="программа для создания чертежей дорожек", font=("@Microsoft YaHei UI Light", 10),fg='#0a0000',bg = '#d6e4ba')
b7.place(x=123,y=35)


#рисунок
s1 = canvas20.create_oval(150,180,350,380,outline="#e8ba73", fill="#e8ba73")
s2 = canvas20.create_oval(150,150,250,250,outline="#c37028", fill="#c37028")
s3 = canvas20.create_oval(400,420,350,370,outline="#4b7674", fill="#4b7674")

root1.mainloop()
