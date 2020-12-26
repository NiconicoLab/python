import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os

#グローバル変数(参照ファイルのパス)
fpath = '/'

#参照釦がクリックされたら実行
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

#実行釦がクリックされたら実行
def file_conduct():
    print("実行!!!")
    root.destroy()

#ウインドウの作成
root = tkinter.Tk()
root.title("Python GUI")
root.geometry("420x240")

#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=100)

#ラベルの作成
input_label = tkinter.Label(text="ファイルパス")
input_label.place(x=10, y=70)

#ボタンの作成
button = tkinter.Button(text="参照",command=file_select)
button.place(x=10, y=50)

button = tkinter.Button(text="実行",command=file_conduct)
button.place(x=10, y=200)

#ウインドウの描画
root.mainloop()

#実行釦が押下された後に実行される
if fpath == '/': #参照ファイルが指定されていない場合
    print("file path error")
else:
    print(fpath)

print("!!!end!!!")
