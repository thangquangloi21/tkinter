from tkinter import *
def len():
    print("lên")
def xuong():
    if (xuongBtn['bg'] == "green"):
        xuongBtn['bg'] = "red"
    else:
        xuongBtn['bg'] = "green"
    print("Xuống")
def trai():
    print("trái")
def phai():
    print("Phải")
win = Tk()
#tao 4 nut nhan
#1
frame1 = Frame(win)
frame1.pack()
#2
frame2 = Frame(win)
frame2.pack()
#3
frame3 = Frame(win)
frame3.pack()
#tao nut len
lenBtn = Button(frame1,text="Lên",command=len,bg= 'red',fg='white')
lenBtn.pack()
#tao nut trai
traiBtn = Button(frame2,text="Trái",command=trai,bg= 'red',fg='white')
traiBtn.pack(side=LEFT)
#tao nut phai
phaiBtn = Button(frame2,text="Phải",command=phai,bg= 'red',fg='white')
phaiBtn.pack(side=RIGHT)
#tao nut xuong
xuongBtn = Button(frame3,text="Xuống",command= xuong,bg= 'white',fg='black')
xuongBtn.pack()
win.mainloop()