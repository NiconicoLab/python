import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import sys

#グローバル変数(参照ファイルのパス)
fpath = '/'
freadflg = False
selected='/'

#参照釦が押下されたら実行
def file_select():
    tkinter.messagebox.showinfo('タイトル','参照ファイルを選択してください')
    dir_path = os.path.dirname(os.path.abspath("__file__")) #ディレクトリの絶対パスを格納
    #print(dir_path) #debug
    idir = dir_path #初期フォルダ
    filetype = [("テキスト","*.txt"), ("全て","*")] #拡張子
    file_path = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
    input_box.insert(tkinter.END, file_path) #結果を表示
    global fpath #グローバル変数であることを定義
    fpath = file_path

#実行釦が押下されたら実行
def file_conduct():
    #ファイルが読み込み可能かどうかチェック
    if os.access(fpath,os.R_OK) == False or fpath == '/':
        tkinter.messagebox.showinfo('タイトル','参照ファイルがありません')
        sys.exit()
    else:
        global freadflg
        freadflg = True
        root.destroy()

#Comboboxの選択が押下されたら実行
def change_select(event):
    global selected
    selected = v.get()
    #print(selected) #debug

if __name__ == '__main__':
    #ウインドウの作成
    root = tkinter.Tk()
    root.title("Python GUI")
    root.geometry("320x60")

    selectlist = ['List A', 'List B', 'List C']
    #選択された値の初期値設定
    selected = selectlist[0]

    # Combobox
    v = tkinter.StringVar()
    cb = ttk.Combobox(root, textvariable=v, values=selectlist)
    cb.set(selectlist[0])
    cb.bind('<<ComboboxSelected>>', change_select)
    cb.place(x=0, y=30)
    cb.DropDownWidth=10;

    #入力欄の作成
    input_box = tkinter.Entry(width=30)
    input_box.place(x=0, y=0)

    #ボタンの作成
    button1 = tkinter.Button(root, text="参照", command=file_select)
    button1.place(x=280, y=3)

    button2 = tkinter.Button(root, text="実行", command=file_conduct)
    button2.place(x=280, y=35)

    #ウインドウの描画
    root.mainloop()

    #pythonプログラムを閉じられた場合のガード処理
    if os.access(fpath,os.R_OK) == False or fpath == '/' or freadflg == False:
        print("guard process") #debug
        sys.exit()

    #実行釦が押下された後に正常時のみ実行される
    print(fpath)
    print(selected)

    print("!!!end!!!")
