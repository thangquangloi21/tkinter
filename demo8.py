from tkinter import *
def hienthi():
    Label(win,
          text=ent.get() + '\n' + ent1.get(),
          font='Time 40 bold').pack()
win = Tk()
ent =  Entry(win,font='Time 40 bold')
ent1 =  Entry(win,font='Time 40 bold')
enter = Button(win,bg='blue',text='Enter',font='Time 40 bold',command= hienthi)
ent.pack()
ent1.pack()
enter.pack()
ent.focus()
win.mainloop()
