'''
自作のパッケージのモジュールの特定の関数のみをimportするお試しするプログラム
モジュール内の特定の関数だけをimportして呼び出したい場合，
fromでパッケージとモジュールを指定し，importで取り込む関数名を指定．
form package.module(library) import functionのように記載する
'''

from my_module.my_function_library import print_lib2

if __name__ == '__main__':
  x = print_lib2(59)
  print(x)

'''
  # print_libはimportしていないため呼ぶことができない
  y = print_lib(12)
  print(y)
'''
