string.pyを実行すると文字列が出力される．
$ python string.py 
start --- string.py ---
end   --- string.py ---
start main --- string.py ---
end   main --- string.py ---

sample.pyを実行するとimport openpyxlをするため，
ガードをかけていない部分は実行されてしまう
 -> start main --- string.py --- の部分は実行されない
 
そのため，自作ライブラリのことも加味して，mainのガードをかけること
$ python sample.py 
start --- string.py ---
end   --- string.py ---
start --- sample.py ---
end   --- sample.py ---

ライブラリとして読み込まれた場合，__pycache__のディレクトリが生成される
その中に，my_function_library.cpython-37.pycのように，
何のプログラムがライブラリとして読み込まれたのかcacheでわかるようになっている

------------------------------------------------------------------------------
[Pythonコーディング規約]PEP8の説明
モジュールをimportする場合の記述は，
import os
import sys
のように複数行にわけ，グループ毎にアルファベット順に並べる．
import os, sysのように1行で書くのは非推奨
グループは，1.標準ライブラリ，2.3rdPartyライブラリ，3.自作のライブラリの順番で
グループ間は空白行で区切る．
