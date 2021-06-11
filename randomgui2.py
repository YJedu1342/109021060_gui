import tkinter as tk
import random
#//////////#
def let_btn_random():
    tmp = random.randint(0,500)
    label_number_strv.set(tmp)
#//////////#
win_main = tk.Tk()
win_main.geometry('600x600')
win_main.title('demo')
#//////////#
label_number_strv = tk.StringVar()
label_number_strv.set('0')
label_number = tk.Label(textvariable=label_number_strv,width=12,height=3)
label_number.pack()

btn_random = tk.Button(text='random',command=let_btn_random)
btn_random.pack()

btn_exit = tk.Button(text='exit',command=win_main.destroy)
btn_exit.pack()

win_main.mainloop()