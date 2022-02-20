from tkinter import *
import tkinter.ttk as exTk
def chon():
    Labelhienthi['text'] = 'Bạn đã Chọn ' + cmb1.get()
win = Tk()
cmb1 = exTk.Combobox(win,width=30,height=20,font='Time 30',state='readonly')
cmb1['values'] = ('CNTT','Cơ Điện Tử','Cơ khí')
btnchon = Button(win,text='Chọn',font='Time 20',command=chon)
cmb1.current(0)
btnchon.grid(row= 0,column=1)
Labelhienthi = Label(win,text = 'Chưa chọn', font = 'Times 30')
cmb1.grid(row= 0,column=0)
Labelhienthi.grid(row= 1,column=0)
win.mainloop()
