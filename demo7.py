from tkinter import *
win = Tk()
def taonhutnhan():
    Button(win,
           text='day la nut nhan: %d'%taonhutnhan.count,
           bg='blue',
           font=50,
           command=taonhutnhan).grid(row=taonhutnhan.count,column=0)
    Label(win,
           text='day la Label: %d'%taonhutnhan.count,
           bg='black',fg= 'white',
           font=50).grid(row=taonhutnhan.count,column=1)
    taonhutnhan.count=taonhutnhan.count+1

taonhutnhan.count = 0
taonhutnhan()
win.mainloop()
