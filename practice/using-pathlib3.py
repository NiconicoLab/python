'''
引数で指定した探索ワードをカレントディレクトリ以下にあるサブディレクトリも含めて検索し一覧を出力するプログラム．
'''

import os
import sys
from pathlib import Path

if __name__ == '__main__':

  args = sys.argv
  if len(args) == 4: #引数を探索ワードにする
    if sys.argv[2] == '0':
      type = 0
      print('path and file name type')
    elif sys.argv[2] == '1':
      print('only file name type')
      type = 1
    else:
      print('type error: type is 0 or 1')
      quit()
  else:
    print('Usage$ python',args[0], '\'serch word\' tpye(0:path and file name,1:only file name) \'search path\'')
    quit()

  serch_word = '**/' + '*' + sys.argv[1] + '*'
  #print(serch_word) #debug

  #検索対象のパスを取得
  folder = Path(sys.argv[3])
  print(folder) #debug

  if type == 0:
    for file_path in folder.glob(serch_word):
      # ファイルの絶対パスを出力
      print(file_path)
  else:
    for file_path in folder.glob(serch_word):
     # ファイル名のみ出力
      print(file_path.name)

