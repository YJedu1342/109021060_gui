import tkinter as tk
from tkinter.constants import CENTER, NW
from PIL import Image,ImageFilter, UnidentifiedImageError
from tkinter import filedialog,messagebox
from glob import glob
#////////////////////////////////////////////#
#Function
#使用者選擇圖片檔案
def getfilepath():
    global img
    filepath =filedialog.askopenfilename()
    tmpflag=True
    try:
        tmp = Image.open(filepath)
    except UnidentifiedImageError:
        tmpflag=False
    if tmpflag:
        label_filepath.config(text=filepath)
    else:
        label_filepath.config(text='請選擇圖片檔')
    del tmp
#////////////////////////////////////////////#
#旋轉
def imgrotatewin():
    #//////////#
    #旋轉的Function
    def rotate_LR():
        try:
            img = Image.open(label_filepath.cget('text'))
            img= img.transpose(Image.FLIP_LEFT_RIGHT)
            pathlist = label_filepath.cget('text').split("/")
            imgName = pathlist[-1]
            dotIndex = imgName.index(".")
            newImgName = imgName[:dotIndex]+ "_rotate_LR" + imgName[dotIndex:]
            img.save(newImgName)
            messagebox.showinfo(title="完成",message='圖片已旋轉完成')
            win_rotate.destroy()
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="請先選擇圖片")
    def rotate_TB():
        try:
            img = Image.open(label_filepath.cget('text'))
            img= img.transpose(Image.FLIP_TOP_BOTTOM)
            pathlist = label_filepath.cget('text').split("/")
            imgName = pathlist[-1]
            dotIndex = imgName.index(".")
            newImgName = imgName[:dotIndex]+ "_rotate_TB" + imgName[dotIndex:]
            img.save(newImgName)
            messagebox.showinfo(title="完成",message='圖片已旋轉完成')
            win_rotate.destroy()
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="請先選擇圖片")
    def rotate_90():
        try:
            img = Image.open(label_filepath.cget('text'))
            img= img.transpose(Image.ROTATE_90)
            pathlist = label_filepath.cget('text').split("/")
            imgName = pathlist[-1]
            dotIndex = imgName.index(".")
            newImgName = imgName[:dotIndex]+ "_rotate_90" + imgName[dotIndex:]
            img.save(newImgName)
            messagebox.showinfo(title="完成",message='圖片已旋轉完成')
            win_rotate.destroy()
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="請先選擇圖片")
    def rotate_180():
        try:
            img = Image.open(label_filepath.cget('text'))
            img= img.transpose(Image.ROTATE_180)
            pathlist = label_filepath.cget('text').split("/")
            imgName = pathlist[-1]
            dotIndex = imgName.index(".")
            newImgName = imgName[:dotIndex]+ "_rotate_180" + imgName[dotIndex:]
            img.save(newImgName)
            messagebox.showinfo(title="完成",message='圖片已旋轉完成')
            win_rotate.destroy()
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="請先選擇圖片")
    def rotate_270():
        try:
            img = Image.open(label_filepath.cget('text'))
            img= img.transpose(Image.ROTATE_270)
            pathlist = label_filepath.cget('text').split("/")
            imgName = pathlist[-1]
            dotIndex = imgName.index(".")
            newImgName = imgName[:dotIndex]+ "_rotate_270" + imgName[dotIndex:]
            img.save(newImgName)
            messagebox.showinfo(title="完成",message='圖片已旋轉完成')
            win_rotate.destroy()
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="請先選擇圖片")
    def rotate_other():
        try:
            img = Image.open(label_filepath.cget('text'))
            rota_degree=float(rotate_degree.get())
            img = img.rotate(rota_degree)
            pathlist = label_filepath.cget('text').split("/")
            imgName = pathlist[-1]
            dotIndex = imgName.index(".")
            newImgName = imgName[:dotIndex]+ "_rotate_" +str(rota_degree)+imgName[dotIndex:]
            img.save(newImgName)
            messagebox.showinfo(title="完成",message='圖片已旋轉完成')
            win_rotate.destroy()
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="請先選擇圖片")
    #//////////#        
    if label_filepath.cget('text') =='檔案路徑'or label_filepath.cget('text') =='請選擇圖片檔':
        messagebox.showerror(title='Error',message='請先選擇圖片')
    else:
        win_rotate = tk.Toplevel(mainwin)
        win_rotate.geometry('200x440')
        win_rotate.title('選擇旋轉度數')

        btn_rotate_LR = tk.Button(win_rotate,text='左右翻轉',font='微軟正黑體 20',command=rotate_LR)
        btn_rotate_LR.pack()
        btn_rotate_TB = tk.Button(win_rotate,text='上下翻轉',font='微軟正黑體 20',command=rotate_TB)
        btn_rotate_TB.pack()
        btn_rotate_90 = tk.Button(win_rotate,text='旋轉90度',font='微軟正黑體 20',command=rotate_90)
        btn_rotate_90.pack()
        btn_rotate_180 = tk.Button(win_rotate,text='旋轉180度',font='微軟正黑體 20',command=rotate_180)
        btn_rotate_180.pack()
        btn_rotate_270 = tk.Button(win_rotate,text='旋轉270度',font='微軟正黑體 20',command=rotate_270)
        btn_rotate_270.pack()
        rotate_degree = tk.StringVar()
        rotate_degree.set('請輸入其他度數')
        entry_rotate_other = tk.Entry(win_rotate,textvariable=rotate_degree,font='微軟正黑體 20')
        entry_rotate_other.pack()
        btn_rotate_other = tk.Button(win_rotate,text='自定義度數',font='微軟正黑體 20',command=rotate_other)
        btn_rotate_other.pack()
#//////////#
#縮放圖片
def imgresize():
    #//////////#
    #等比例縮放圖片的Function
    def resize_ratio():
        img = Image.open(label_filepath.cget('text'))
        new_width = int(resiz_ratio.get())
        ratio = float(new_width) / img.size[0]
        new_height = int(img.size[1] * ratio)
        img = img.resize((new_width,new_height),Image.BICUBIC)
        pathlist = label_filepath.cget('text').split("/")
        imgName = pathlist[-1]
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex]+ "_resized" + imgName[dotIndex:]
        img.save(newImgName)
        messagebox.showinfo(title="完成",message='圖片已旋轉完成')
        win_resize.destroy()
    if label_filepath.cget('text') =='檔案路徑'or label_filepath.cget('text') =='請選擇圖片檔':
        messagebox.showerror(title='Error',message='請先選擇圖片')
    else:
        win_resize = tk.Toplevel(mainwin)
        win_resize.geometry('350x180')
        win_resize.title('縮放比例設定')

        resiz_ratio = tk.StringVar()
        entry_resize_ratio = tk.Entry(win_resize, textvariable=resiz_ratio,font='微軟正黑體 20')
        entry_resize_ratio.pack()
        btn_resize_ratio = tk.Button(win_resize, text="產生圖片",font='微軟正黑體 20',command=resize_ratio)
        btn_resize_ratio.pack()
#//////////#
#縮小圖片至1/5
def imgthumbnail():
    if label_filepath.cget('text') =='檔案路徑'or label_filepath.cget('text') =='請選擇圖片檔':
        messagebox.showerror(title='Error',message='請先選擇圖片')
    else:
        img = Image.open(label_filepath.cget('text'))
        img.thumbnail((img.size[0]/5,img.size[1]/5))
        pathlist = label_filepath.cget('text').split("/")
        imgName = pathlist[-1]
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex]+ "_thumbnail" + imgName[dotIndex:]
        img.save(newImgName)
        messagebox.showinfo(title="完成",message='縮圖已製作完成')
#//////////#
#濾鏡
def imgfliter():
    pass
    #//////////#
    #function
    def fliter_Blur():
        img= Image.open(label_filepath.cget('text'))
        pathlist = label_filepath.cget('text').split("/")
        imgName = pathlist[-1]
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex]+ "_resized" + imgName[dotIndex:]
        img.save(newImgName)
        messagebox.showinfo(title="完成",message='圖片已完成')
        win_fliter.destroy()
    #//////////#
    if label_filepath.cget('text') =='檔案路徑'or label_filepath.cget('text') =='請選擇圖片檔':
        messagebox.showerror(title='Error',message='請先選擇圖片')
    else:
        win_fliter = tk.Toplevel(mainwin)
        win_fliter.geometry('200x600')
        win_fliter.title('選擇濾鏡')

        btn_fliter_Blur = tk.Button(win_fliter,text='模糊(Blur)',command=fliter_Blur,font='微軟正黑體 20')
        btn_fliter_Blur.pack()
        btn_fliter_Countour= tk.Button(win_fliter,text='輪廓(Contour)',command=fliter_Contour,font='微軟正黑體 20')
        btn_fliter_Countour.pack()
        btn_fliter_Detail = tk.Button(win_fliter,text='細節增強(Detail)',command=fliter_Detai,font='微軟正黑體 20')
        btn_fliter_Detail.pack()
        btn_fliter_Edge_Enhance = tk.Button(win_fliter,text='邊緣增強(Edge_Enhance)',command=fliter_Edge_Enhance,font='微軟正黑體 20')
        btn_fliter_Edge_Enhance.pack()
        btn_fliter_Edge_Enhance_more = tk.Button(win_fliter,text='深度邊緣增強(Edge_Enhance_more)',command=fliter_Edge_Enhance_more,font='微軟正黑體 20')
        btn_fliter_Edge_Enhance_more.pack()
        btn_fliter_Emboss = tk.Button(win_fliter,text='浮雕效果(Emboss)',command=fliter_Emboss,font='微軟正黑體 20')
        btn_fliter_Emboss.pack()
        btn_fliter_Find_Edges = tk.Button(win_fliter,text='邊緣訊息(Find_Edges)',command=fliter_Find_Edges,font='微軟正黑體 20')
        btn_fliter_Find_Edges.pack()
        btn_fliter_Smooth = tk.Button(win_fliter,text='平滑效果(Smooth)',command=fliter_Smooth,font='微軟正黑體 20')
        btn_fliter_Smooth.pack()
        btn_fliter_Smooth_more = tk.Button(win_fliter,text='深度平滑效果(Smooth_more)',command=fliter_Smooth_more,font='微軟正黑體 20')
        btn_fliter_Smooth_more.pack()
        btn_fliter_Sharpen = tk.Button(win_fliter,text='銳利化效果(Sharpen)',command=fliter_Sharpen,font='微軟正黑體 20')
        btn_fliter_Sharpen.pack()
#//////////#
#變更圖片格式
def chanformat():
    #//////////#
    #變更圖片格式
    def chanformat_png2jpg():
        img = Image.open(label_filepath.cget('text'))
        pathlist = label_filepath.cget('text').split("/")
        imgName = pathlist[-1]
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex]+ "_jpg" + ".jpg"
        img = img.convert("RGB")
        img.save(newImgName)
        messagebox.showinfo(title="完成",message='圖片已轉換成jpg檔')
        win_chanformat.destroy()
    def chanformat_jpg2png():
        img = Image.open(label_filepath.cget('text'))
        pathlist = label_filepath.cget('text').split("/")
        imgName = pathlist[-1]
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex]+ "_png" + ".png"
        img.save(newImgName)
        messagebox.showinfo(title="完成",message='圖片已轉換成png檔')
        win_chanformat.destroy()
    #//////////#
    if label_filepath.cget('text') =='檔案路徑'or label_filepath.cget('text') =='請選擇圖片檔':
        messagebox.showerror(title='Error',message='請先選擇圖片')
    else:
        win_chanformat = tk.Toplevel(mainwin)
        win_chanformat.geometry('350x280')
        win_chanformat.title('格式轉換')
        pathlist = label_filepath.cget('text').split("/")
        imgName = pathlist[-1]
        dotIndex = imgName.index(".")
        label_fileformat_text='現在的檔案類型為:'+imgName[dotIndex: ]
        label_fileformat = tk.Label(win_chanformat,text=label_fileformat_text,font='微軟正黑體 20')
        label_fileformat.pack()
        if imgName[dotIndex:]=='.png':
            btn_fileformat_png2jpg = tk.Button(win_chanformat,text='png轉換為jpg',font='微軟正黑體 20',command=chanformat_png2jpg)
            btn_fileformat_png2jpg.pack()
        elif imgName[dotIndex:]=='.jpg':
            btn_fileformat_jpg2png = tk.Button(win_chanformat,text='jpg轉換為png',font='微軟正黑體 20',command=chanformat_jpg2png)
            btn_fileformat_jpg2png.pack()
#////////////////////////////////////////////#
#主視窗
mainwin = tk.Tk()
mainwin.title('簡易圖片處理工具 EasyImagetools')
mainwin.geometry('500x460')
#////////////////////////////////////////////#
#主頁面配置
btn_rotate = tk.Button(text='圖片旋轉',font='微軟正黑體 20',command=imgrotatewin)
btn_rotate.place(anchor=NW,x=340,y=10,width=150,height=80)

btn_resize = tk.Button(text='圖片縮放',font='微軟正黑體 20',command=imgresize)
btn_resize.place(anchor=NW,x=340,y=100,width=150,height=80)

btn_thumbnail = tk.Button(text='圖片縮圖',font='微軟正黑體 20',command=imgthumbnail)
btn_thumbnail.place(anchor=NW,x=340,y=190,width=150,height=80)

btn_fliter = tk.Button(text='套用濾鏡',font='微軟正黑體 20',command=imgfliter)
btn_fliter.place(anchor=NW,x=340,y=280,width=150,height=80)

btn_chanformat = tk.Button(text='轉換圖片格式',font='微軟正黑體 18',command=chanformat)
btn_chanformat.place(anchor=NW,x=340,y=370,width=150,height=80)

btn_choosefile = tk.Button(text='請選擇檔案',font='微軟正黑體 20',command=getfilepath)
btn_choosefile.place(anchor=CENTER,x=170,y=60,width=180,height=50)

label_filepath = tk.Label(text = '檔案路徑')
label_filepath.configure(font=('Comic Sans MS',16))
label_filepath.place(anchor=CENTER,x=170,y=130)
mainwin.mainloop()