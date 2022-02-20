from tkinter import *
import threading
win = Tk()
label1 = Label(win,text="Chao cac ban left")
label1.pack(side= LEFT)
label2 = Label(win,text="Chao cac ban ringht")
label2.pack(side= RIGHT)
def setText():
    while (True):
        content = input()
        label1.config(text=content)
setTextThr = threading.Thread(target=setText)
setTextThr.start()
win.mainloop()