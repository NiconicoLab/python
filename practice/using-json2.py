import json

if __name__ == '__main__':

  fpath = './usingjson.json' #jsonファイルのパス

  try:
      with open(fpath) as db:
          jsn = json.load(db) #jsonファイル読み込み
          #print(jsn) #debug
  except IndexError:
      print('not found')

  for jsn_key in jsn:
      print(jsn_key, end='')
      print('     ', end='')
      print(jsn[jsn_key]["parameter3"][0], end='')
      print('     ', end='')
      print(jsn[jsn_key]["parameter3"][1], end='')
      print('     ', end='')
      print(jsn[jsn_key]["parameter3"][2])

  import re

  with open('./usingjson2.txt') as data:
      lines = data.read()
      for l in lines.split("\n"):
          print(l)
          words = re.split(" +", l) #正規表現モジュールで複数個のスペースに対応
          if words[0]: #配列が空でない時
            print(words, end='     ')
            print(words[0], end=',')
            print(words[1], end=',')
            print(words[2])
