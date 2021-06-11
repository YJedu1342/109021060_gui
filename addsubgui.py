import tkinter as tk
#//////////#
def let_btn_add():
    count = int(label_count_strv.get())
    count += 1
    label_count_strv.set(count)
def let_btn_sub():
    count = int(label_count_strv.get())
    count -= 1
    label_count_strv.set(count)
def let_btn_color_red():
    colorarr = ['0','1','2','2','4','5','6','7','8','9','A','B','C','D','E','F']
    OrgColor = label_count.cget('bg')[1]
    print(OrgColor)

def let_btn_color_green():
    pass
def let_btn_color_blue():
    pass
#//////////#
win_main = tk.Tk()
win_main.geometry('600x600')
win_main.config(bg="#F0f0f0")
win_main.title('demo')
#//////////#
label_count_strv = tk.StringVar()
label_count_strv.set('0')
label_count = tk.Label(textvariable=label_count_strv,width=12,height=3,bg='#000000')
label_count.pack()

btn_add = tk.Button(text='add',command=let_btn_add)
btn_add.pack()

btn_sub = tk.Button(text='sub',command=let_btn_sub)
btn_sub.pack()

btn_color_red = tk.Button(text='red',command=let_btn_color_red)
btn_color_red.pack()

btn_color_green = tk.Button(text='green',command=let_btn_color_green)
btn_color_green.pack()

btn_color_blue = tk.Button(text='blue',command=let_btn_color_blue)
btn_color_blue.pack()

btn_exit = tk.Button(text='exit',command=win_main.destroy)
btn_exit.pack()

win_main.mainloop()