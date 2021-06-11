import tkinter as tk
import random
#//////////#
def let_btn_random():
    list_number = random.sample(range(1,42),6)
    label_number_strv.set(list_number[0])
    label_number_strv_2.set(list_number[1])
    label_number_strv_3.set(list_number[2])
    label_number_strv_4.set(list_number[3])
    label_number_strv_5.set(list_number[4])
    label_number_strv_6.set(list_number[5])
#//////////#
win_main = tk.Tk()
win_main.geometry('600x600')
win_main.title('demo')
#//////////#
label_number_strv = tk.StringVar()
label_number_strv.set('0')
label_number = tk.Label(textvariable=label_number_strv,width=12,height=3)
label_number.pack()

label_number_strv_2 = tk.StringVar()
label_number_strv_2.set('0')
label_number_2 = tk.Label(textvariable=label_number_strv_2,width=12,height=3)
label_number_2.pack()

label_number_strv_3 = tk.StringVar()
label_number_strv_3.set('0')
label_number_3 = tk.Label(textvariable=label_number_strv_3,width=12,height=3)
label_number_3.pack()

label_number_strv_4 = tk.StringVar()
label_number_strv_4.set('0')
label_number_4 = tk.Label(textvariable=label_number_strv_4,width=12,height=3)
label_number_4.pack()

label_number_strv_5 = tk.StringVar()
label_number_strv_5.set('0')
label_number_5 = tk.Label(textvariable=label_number_strv_5,width=12,height=3)
label_number_5.pack()

label_number_strv_6 = tk.StringVar()
label_number_strv_6.set('0')
label_number_6 = tk.Label(textvariable=label_number_strv_6,width=12,height=3)
label_number_6.pack()

btn_random = tk.Button(text='random',command=let_btn_random)
btn_random.pack()

btn_exit = tk.Button(text='exit',command=win_main.destroy)
btn_exit.pack()

win_main.mainloop()