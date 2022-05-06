'''
自作のパッケージを使うことをお試しするプログラム
form packageとなるため，ここにディレクトリ名を入れる．
そして，そのディレクトリの中で使うモジュール(ライブラリ)名をimportする．
import AAA as BBBの書式を使うため，使う際はBBB.func()のように記載する
'''

from my_module import my_function_library as my

if __name__ == '__main__':
  x = my.print_lib(12345)
  print(x)