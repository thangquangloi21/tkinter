from tkinter import *
win = Tk()
lb1 = Label(win,text= 'Doan van thu nhat\n doan van thu hai',bg = 'red',fg= 'black',
            font='Time 50 bold italic',
            width=45,
            relief= "ridge", #chinh do bong
            borderwidth=10) #chinh bong to nho
lb2 = Label(win,text= 'Doan van thu ba')
lb3 = Label(win,text= 'Doan van thu tu\n doan van thu nam',bg = 'red',fg= 'black',
            font='Time 50 bold italic',
            width=45,
            relief= "ridge", #chinh do bong
            borderwidth=10, #chinh bong to nho
            height=7,
            anchor=CENTER, #chinh theo huong
            padx=100,
            pady=100,
            justify= LEFT #can le
            )

lb1.pack()
lb2.pack()
lb3.pack()
win.mainloop()
