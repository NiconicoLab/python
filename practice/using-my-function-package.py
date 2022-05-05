'''
自作のパッケージを使うことをお試しするプログラム
form packageとなるため，ここにディレクトリ名を入れる．
そして，そのディレクトリの中で使うモジュール(ライブラリ)名をimportする．
import AAAの書式を使うため，使う際はAAA.func()のように記載する
'''

from my_module import my_function_library

if __name__ == '__main__':
  x = my_function_library.print_lib(10)
  print(x)