'''
自作関数のインポートして使うことをお試しするプログラム
import AAA as BBBの書式を使うため，使う際はBBB.func()のように記載する
'''

import my_function_library as my

if __name__ == '__main__':
  x = my.print_lib(12345)
  print(x)