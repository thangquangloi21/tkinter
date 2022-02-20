from tkinter import *
win = Tk()
win.title('thang quang loi')
#win.configure(width=500,height=600)
scrW = win.winfo_screenwidth()
scrH = win.winfo_screenheight()
win.geometry('500x600+%d+%d'%(scrW/2-250,scrH/2-300))
win.configure(bg='#0000ff')#pha mau theo mau rgb
# win.resizable(width=False,height=False)
win.mainloop()
