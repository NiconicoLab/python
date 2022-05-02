'''
自作関数のインポートして使うことをお試しするプログラム
import AAAの書式を使うため，使う際はAAA.func()のように記載する
'''

import my_function_library

if __name__ == '__main__':
  x = my_function_library.print_lib(10)
  print(x)