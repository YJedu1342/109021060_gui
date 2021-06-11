import tkinter as tk
from tkinter.constants import RIGHT
#//////////#
list_count=[0]*4
list_count[1] ='+'
def btn(num):
    if int(label_shownumber['text']) !=0:
        if list_count[1] == 0:
            tmp=list_count[0]+num
            label_shownumber.config(text=tmp)
            list_count[0]=tmp
        elif list_count[1] == '+':
            if list_count[3] == 0 and list_count[2]==0:
                tmp1 = list_count[0]+'+'+num
                label_shownumber.config(text=tmp1)
                list_count[2]=num
            elif list_count[3] ==0 and list_count[2]!=0:
                tmp2 = str(list_count[2]+num)
                list_count[2]=tmp2
                strtmp = list_count[0]+'+'+tmp2
                label_shownumber.config(texts=strtmp)
    else:
        label_shownumber.config(text=num)
        list_count[0]=num
#//////////#
win_main = tk.Tk()
win_main.geometry('440x600+200+100')
win_main.title('calculator')
#//////////#
win_main.rowconfigure(0,weight=1)
win_main.rowconfigure(1,weight=1)
win_main.rowconfigure(2,weight=1)
win_main.rowconfigure(3,weight=1)
win_main.rowconfigure(4,weight=1)
win_main.rowconfigure(5,weight=1)
win_main.columnconfigure(0,weight=1)
win_main.columnconfigure(1,weight=1)
win_main.columnconfigure(2,weight=1)
win_main.columnconfigure(3,weight=1)


#//////////#
label_shownumber = tk.Label(text='0',
                            anchor='e',
                            justify=RIGHT)
label_shownumber.grid(row=0,column=0,columnspan=4,sticky='NSEW')

btn_ce = tk.Button(text='CE',command=btn)
btn_ce.grid(row=1,column=0,sticky = "NSEW")

btn_C = tk.Button(text='C',command=btn)
btn_C.grid(row=1,column=1,sticky='NSEW')

btn_back = tk.Button(text='<---',command=btn)
btn_back.grid(row=1,column=2,sticky='NSEW')

btn_division = tk.Button(text='/',command=btn)
btn_division.grid(row=1,column=3,sticky='NSEW')
#//////////#
btn_seven = tk.Button(text='7',command=lambda:btn('7'))
btn_seven.grid(row=2,column=0,sticky='NSEW')

btn_eight = tk.Button(text='8',command=lambda:btn('8'))
btn_eight.grid(row=2,column=1,sticky='NSEW')

btn_nine = tk.Button(text='9',command=btn)
btn_nine.grid(row=2,column=2,sticky='NSEW')

btn_cross = tk.Button(text='cross',command=btn)
btn_cross.grid(row=2,column=3,sticky='NSEW')
#//////////#
btn_four = tk.Button(text='4',command=btn)
btn_four.grid(row=3,column=0,sticky='NSEW')

btn_five = tk.Button(text='5',command=btn)
btn_five.grid(row=3,column=1,sticky='NSEW')

btn_six = tk.Button(text='6',command=btn)
btn_six.grid(row=3,column=2,sticky='NSEW')

btn_minus = tk.Button(text='-',command=btn)
btn_minus.grid(row=3,column=3,sticky='NSEW')
#//////////#
btn_one = tk.Button(text='1',command=btn)
btn_one.grid(row=4,column=0,sticky='NSEW')

btn_two = tk.Button(text='2',command=btn)
btn_two.grid(row=4,column=1,sticky='NSEW')

btn_three = tk.Button(text='3',command=btn)
btn_three.grid(row=4,column=2,sticky='NSEW')

btn_plus = tk.Button(text='+',command=btn)
btn_plus.grid(row=4,column=3,sticky='NSEW')
#//////////#
btn_negative = tk.Button(text='+/-',command=btn)
btn_negative.grid(row=5,column=0,sticky='NSEW')

btn_zero = tk.Button(text='0',command=btn)
btn_zero.grid(row=5,column=1,sticky='NSEW')

btn_dot = tk.Button(text='.',command=btn)
btn_dot.grid(row=5,column=2,sticky='NSEW')

btn_equals = tk.Button(text='=',command=btn)
btn_equals.grid(row=5,column=3,sticky='NSEW')
#//////////#
win_main.mainloop()