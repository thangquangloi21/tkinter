from tkinter import *
win = Tk()
#dong goi theo kieu luoi
# Label(win,text='doan van 1',font='Time 20',bg = 'red').grid(row = 0,column = 0)
# Label(win,text='doan van 2',font= 'Time 25',bg = 'green').grid(row = 1,column = 0)
# Label(win,text='doan van A',font='Time 30',bg = 'blue').grid(row = 0,column = 1)
# Label(win,text='doan van B',font='Time 35',bg = 'white').grid(row = 1,column = 1)
# Label(win,text='doan van 3',font='Time 40',bg = 'yellow').grid(row = 1,column = 2)
# Label(win,text='doan van 4',font='Time 45',bg = 'pink').grid(row = 2,column = 2)

Label(win,text= 'doan van',bg = 'red',font='Times 30').place(relwidth=.5
                                                             ,relheight =.5
                                                             ,relx=.1
                                                             ,rely=.1)
win.mainloop()