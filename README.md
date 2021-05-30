$ git clone https://github.com/NiconicoLab/python.git
$ git add xxx
$ git commit -m "xxx"
$ git push -u origin master

■python2系
# -*- coding: utf-8 -*- のようにUTF-8でエンコード宣言を行うこと(マルチバイト文字が要因)

■python3系
エンコード宣言を省略した場合，デフォルトでUTF-8が適用されるため、毎回の記述は不要

■その他
__name__ == __main__
これは別モジュールからのインポートには実行しないための仕組み
※別のモジュールから呼び出された時，自身のモジュール名が入るので実行されない
　実行された時には__name__には__main__が入っている

pythonははじめのロードモジュールから始まるため，if __name__ == __main__: よりも，
ファイルの先頭にprint等があれば，そちら先に実行されるという意味

インタープリタ記述
ファイルの先頭に記述される下記のことを指し，pythonを実行される時に参照されるパスを書く
#! /usr/bin/python
