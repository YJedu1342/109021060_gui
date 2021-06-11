import tkinter as tk
from tkinter import messagebox
#//////////#
#Function
flag=True
def set_btn_text(num):
    global flag
    if flag:
        tmp="O"
    else:
        tmp='X'
    
    if num == 0:
        btn_1_str.set(tmp)
        btn_1.config(state='disabled')
    elif num ==1:
        btn_2_str.set(tmp)
        btn_2.config(state='disabled')
    elif num ==2:
        btn_3_str.set(tmp)
        btn_3.config(state='disabled')
    elif num ==3:
        btn_4_str.set(tmp)
        btn_4.config(state='disabled')
    elif num ==4:
        btn_5_str.set(tmp)
        btn_5.config(state='disabled')
    elif num ==5:
        btn_6_str.set(tmp)
        btn_6.config(state='disabled')
    elif num ==6:
        btn_7_str.set(tmp)
        btn_7.config(state='disabled')
    elif num ==7:
        btn_8_str.set(tmp)
        btn_8.config(state='disabled')
    elif num ==8:
        btn_9_str.set(tmp)
        btn_9.config(state='disabled')
    flag= not flag
    if btn_1_str.get() == btn_2_str.get() and btn_1_str.get() == btn_3_str.get() and btn_1_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_1_str.get()+'贏了')
    elif btn_4_str.get() == btn_5_str.get() and btn_4_str.get() == btn_6_str.get() and btn_4_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_4_str.get()+'贏了')
    elif btn_7_str.get() == btn_8_str.get() and btn_7_str.get() == btn_9_str.get() and btn_7_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_7_str.get()+'贏了')
    elif btn_1_str.get() == btn_4_str.get() and btn_1_str.get() == btn_7_str.get() and btn_1_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_1_str.get()+'贏了')
    elif btn_2_str.get() == btn_5_str.get() and btn_2_str.get() == btn_8_str.get() and btn_2_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_2_str.get()+'贏了')
    elif btn_3_str.get() == btn_6_str.get() and btn_3_str.get() == btn_9_str.get() and btn_3_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_3_str.get()+'贏了')
    elif btn_1_str.get() == btn_5_str.get() and btn_1_str.get() == btn_9_str.get() and btn_1_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_1_str.get()+'贏了')
    elif btn_3_str.get() == btn_5_str.get() and btn_3_str.get() == btn_7_str.get() and btn_3_str.get() != "":
        messagebox.showinfo(title='勝者',message= btn_3_str.get()+'贏了')
#//////////#
#主視窗
win_main = tk.Tk()
win_main.geometry('400x400+200+100')
win_main.title('Tic-Tac-Toe')
#//////////#
win_main.rowconfigure(0,weight=1)
win_main.rowconfigure(1,weight=1)
win_main.rowconfigure(2,weight=1)
win_main.columnconfigure(0,weight=1)
win_main.columnconfigure(1,weight=1)
win_main.columnconfigure(2,weight=1)

btn_1_str=tk.StringVar()
btn_1 = tk.Button(textvariable=btn_1_str,command=lambda:set_btn_text(0))
btn_1.grid(row=0,column=0,sticky = "NSEW")

btn_2_str=tk.StringVar()
btn_2 = tk.Button(textvariable=btn_2_str,command=lambda:set_btn_text(1))
btn_2.grid(row=0,column=1,sticky='NSEW')

btn_3_str=tk.StringVar()
btn_3 = tk.Button(textvariable=btn_3_str,command=lambda:set_btn_text(2))
btn_3.grid(row=0,column=2,sticky='NSEW')

btn_4_str=tk.StringVar()
btn_4 = tk.Button(textvariable=btn_4_str,command=lambda:set_btn_text(3))
btn_4.grid(row=1,column=0,sticky='NSEW')

btn_5_str=tk.StringVar()
btn_5 = tk.Button(textvariable=btn_5_str,command=lambda:set_btn_text(4))
btn_5.grid(row=1,column=1,sticky='NSEW')

btn_6_str=tk.StringVar()
btn_6 = tk.Button(textvariable=btn_6_str,command=lambda:set_btn_text(5))
btn_6.grid(row=1,column=2,sticky='NSEW')

btn_7_str=tk.StringVar()
btn_7 = tk.Button(textvariable=btn_7_str,command=lambda:set_btn_text(6))
btn_7.grid(row=2,column=0,sticky='NSEW')

btn_8_str=tk.StringVar()
btn_8 = tk.Button(textvariable=btn_8_str,command=lambda:set_btn_text(7))
btn_8.grid(row=2,column=1,sticky='NSEW')

btn_9_str=tk.StringVar()
btn_9 = tk.Button(textvariable=btn_9_str,command=lambda:set_btn_text(8))
btn_9.grid(row=2,column=2,sticky='NSEW')

win_main.mainloop()