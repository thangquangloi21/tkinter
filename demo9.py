from tkinter import *
win = Tk()
cans = Canvas(win,width=500,height=500,bg='red')
cans1 = Canvas(win,width=500,height=500,bg='blue')
cans.create_line(10,10,400,400,fill='black',width=10, arrow='last',arrowshape=(100,100,40)) # tao duong thang
cans1.create_line(10,10,400,400,70,89,12,500,fill='black',width=10)
cans.grid(row=0,column=0)
cans1.grid(row=0,column=1)
win.mainloop()
