import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

#グローバル変数(参照ファイルのパス)
fpath = '/'
freadflg = False

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
    if os.access(fpath,os.R_OK) == False or fpath == '/' or freadflg == False:
        print("guard process") #debug
        sys.exit()

    #実行釦が押下された後に正常時のみ実行される
    print(fpath)

    #読み取りモードでファイルを開く
    print("debug program 1")
    f = open(fpath, 'r')
    #1行読み込み
    line = f.readline()
    print(line)
    print(line.strip()) #文字列.strip()で空白文字，改行コードを削除
    #ファイルを閉じる
    f.close()

    #最後まで読み込む例
    print("debug program 2")
    f = open(fpath, 'r')
    line = f.readline()
    while line:
        print(line.strip()) #空白，改行コードは削除しておく
        line = f.readline()
    f.close()

    #with構文を使用すると開始/終了時の必須処理を絶対に実行される
    print("debug program 3")
    with open(fpath, "r") as f:
        while True:
            fragment = f.read(1)
            print(fragment, end='') ##改行なしで出力したい時に「end=''」オプションを使用
            if not fragment: #ファイルの最後の文字だった場合
                break

    print("!!!end!!!")
