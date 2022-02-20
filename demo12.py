from tkinter import *
import tkinter.ttk as exTk
import tkinter.scrolledtext as scllText
class monitor(Frame):
    def placeGUI(obj,ev):
        if ev.widget == obj:
            objw = ev.width
            objh = ev.height
            obj.sebdBtn.place(height=25,width=50,x=objw-55,y=0)
            obj.inputText.place(height=25,width=objw - 60,x=5,y=0)
            obj.outputText.place(height=objh-95, width=objw - 10, x=5, y=30)
            obj.houputText.place(height=20, width=objw - 20, x=5, y=objh-65)
            obj.ClearBtn.place(height=25,width=100,x=objw-110,y=objh - 30)
            obj.badCbb.place(height=25, width=120, x=objw - 240, y=objh - 30)
            obj.sigCbb.place(height=25, width=120, x=objw - 380, y=objh - 30)
            obj.autoscrooll.place(height=25, width=100, x=5, y=objh - 30)
            obj.showtimetampchk.place(height=25, width=125, x=125, y=objh - 30)
    def __init__(obj,master):
        super().__init__(master)
        obj.inputText = exTk.Entry(obj)
        obj.houputText =Scrollbar(obj,orient= HORIZONTAL)
        obj.outputText = scllText.ScrolledText(obj,wrap='none',xscrollcommand= obj.houputText.set)
        obj.houputText['command'] = obj.outputText.xview()
        obj.sebdBtn = exTk.Button(obj,text='Send')
        obj.ClearBtn = exTk.Button(obj, text='Clear Output')
        obj.badCbb = exTk.Combobox(obj)
        obj.sigCbb = exTk.Combobox(obj)
        obj.autoscrooll = exTk.Checkbutton(obj,text='Auto scroll')
        obj.showtimetampchk = exTk.Checkbutton(obj, text='Show timestamp')
        master.bind("<Configure>",obj.placeGUI)
win = Tk()
icon = Image("photo",file = 'aduno1.png')
win.title("aduno")
win.wm_iconphoto(True,icon)
win.geometry('1000x700')
aduino = monitor(win)
aduino.place(relwidth=1,relheight=1)
win.mainloop()
