'''
カレントディレクトリ以下にあるサブディレクトリも含めて指定した拡張子のファイル一覧を出力するプログラム．
出力例として(1)ファイル名を含めた絶対パスと(2)ファイル名のみの2パターンを載せている．
for 格納される変数 in カレントディレクトリのパス.glob('*.py'):の場合は．
カレントディレクトリのファイルのみを探索対象とする．
for 格納される変数 in カレントディレクトリのパス.glob('**/*.py'):の場合は
サブディレクトリを含めたファイルを探索対象とする．
'''

import os
from pathlib import Path

if __name__ == '__main__':

  #本pythonスクリプトのカレントディレクトリのパスを取得
  current_folder_path = os.getcwd()
  print(current_folder_path)

  folder = Path(current_folder_path)

  print('--- *.txt ---')
  for file_path in folder.glob('*.txt'):
    # ファイルの絶対パスを出力
    print(file_path)
  for file_path in folder.glob('*.txt'):
   # ファイル名のみ出力
    print(file_path.name)

  print('--- *.py ---')
  #for file_path in folder.glob('*.py'):
  for file_path in folder.glob('**/*.py'):
    # ファイルの絶対パスを出力
    print(file_path)
  #for file_path in folder.glob('*.py'):
  for file_path in folder.glob('**/*.py'):
    # ファイル名のみ出力
    print(file_path.name)
