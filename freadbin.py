import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

#グローバル変数(参照ファイルのパス)
fpath = '/'

#参照釦が押下されたら実行
def file_select():
    tkinter.messagebox.showinfo('タイトル','参照ファイルを選択してください')
    dir_path = os.path.dirname(os.path.abspath("__file__")) #ディレクトリの絶対パスを格納
    #print(dir_path) #debug
    idir = dir_path #初期フォルダ
    filetype = [("バイナリ","*.bin"), ("全て","*")] #拡張子
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
        root.destroy()

if __name__ == '__main__':
    #ウインドウの作成
    root = tkinter.Tk()
    root.title("Python GUI")
    root.geometry("480x50")

    #入力欄の作成
    input_box = tkinter.Entry(width=40)
    input_box.place(x=5, y=10)

    #ラベルの作成
    #input_label = tkinter.Label(text="ファイルパス")
    #input_label.place(x=10, y=0)

    #ボタンの作成
    button = tkinter.Button(text="参照",command=file_select)
    button.place(x=380, y=10)

    button = tkinter.Button(text="実行",command=file_conduct)
    button.place(x=420, y=10)

    #ウインドウの描画
    root.mainloop()

    #pythonプログラムを閉じられた場合のガード処理
    if os.access(fpath,os.R_OK) == False or fpath == '/':
        print("guard process") #debug
        sys.exit()

    #実行釦が押下された後に正常時のみ実行される
    print(fpath)

    #バイナリオプションで読み込む
    print("binary read mode")
    with open(fpath, "rb") as f:
        while True:
            fragment = f.read(1)
            print(fragment, end='') ##改行なしで出力したい時に「end=''」オプションを使用
            if not fragment: #ファイルの最後の文字だった場合
                break

    print("!!!end!!!")
