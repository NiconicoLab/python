import json

if __name__ == '__main__':
  
  fpath = '../data/sample.json' #jsonファイルのパス
  
  try:
      with open(fpath) as f:
          jsn = json.load(f) #jsonファイル読み込み
          #print(jsn) #debug
  except IndexError:
      print('not found')
  
  # key一覧を出力
  print('--- key ---')
  for jsn_key in jsn:
      print(jsn_key)
  
  # 値の一覧を出力
  print('--- val ---')
  for jsn_val in jsn.values():
      print(jsn_val)
  
  # keyから値を出力
  print('--- val from key---')
  print(jsn["No.3"])
  print(jsn["No.2"]["parameter1"])
  
  # jsonファイルのparameter2のみ表示
  print('--- key ---')
  for jsn_key in jsn:
      print(jsn[jsn_key]["parameter2"])
  
  # jsonファイルの入れ子構造の表示
  print('--- advance ---')
  print(jsn["No.4"]["parameter3"][0])
  print(jsn["No.4"]["parameter3"][1])
  print(jsn["No.5"]["parameter3"]["data"]["data1"][0])
  print(jsn["No.5"]["parameter3"]["data"]["data2"][1])
  