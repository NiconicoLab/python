# coding: utf-8
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import sys

selectlist = ['List A', 'List B', 'List C']

#グローバル変数(参照ファイルのパス)
fpath = '/'
freadflg = False    
selected = selectlist[0]

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
    selected = var.get()
    #print(selected) #debug

if __name__ == '__main__':
    #ウインドウの作成
    root = tkinter.Tk()
    root.title("Python GUI")
    root.geometry("500x120")

    # メインフレーム
    main_frm = ttk.Frame(root)
    main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

    # ウィジェット作成（フォルダパス）
    input_label = ttk.Label(main_frm, text="フォルダ指定")
    input_box = ttk.Entry(main_frm)
    input_btn = ttk.Button(main_frm, text="参照", command=file_select)

    # ウィジェット作成（Combobox）
    var = tkinter.StringVar()
    order_label = ttk.Label(main_frm, text="リスト")
    order_comb = ttk.Combobox(main_frm, textvariable=var, values=selectlist, width=10)
    order_comb.set(selectlist[0])
    order_comb.bind('<<ComboboxSelected>>', change_select)

    # ウィジェット作成（実行ボタン）
    exe = ttk.Button(main_frm, text="実行", command=file_conduct)

    # ウィジェットの配置
    input_label.grid(column=0, row=0, pady=10)
    input_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
    input_btn.grid(column=2, row=0)
    order_label.grid(column=0, row=1)
    order_comb.grid(column=1, row=1, sticky=tkinter.W, padx=5)
    exe.grid(column=1, row=2)

    # 配置設定
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main_frm.columnconfigure(1, weight=1)

    root.mainloop()

    #pythonプログラムを閉じられた場合のガード処理
    if os.access(fpath,os.R_OK) == False or fpath == '/' or freadflg == False:
        print("guard process") #debug
        sys.exit()

    #実行釦が押下された後に正常時のみ実行される
    print(fpath)
    print(selected)

    print("!!!end!!!")
