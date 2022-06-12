#指定箇所のみ抽出

import sys

'''
引数は検索対象の文字列
.find(str)  : 前方から検索
.rfind(str) : 後方から検索
'''
def search(msg, str):
  if -1!=msg.find(str): #strの文字列で検索する．-1でない時は検索にヒットした時
    r=msg[msg.find(str): -1] # [a:b]でa~bの範囲指定．bに-1を入れると配列の1番後ろを指す
    print(r)

'''
引数はファイル名，検索する文字
'''
def search_file(fname, str):
  f = open(fname, 'r')
  datalist = f.readlines()
  for data in datalist:
    #print(data, end='')
    #print(data) #readlinesで取得した文字列には改行コードまで含まれるため，printで出力すると余計な改行が入る
    search(data, str) #readlinesで取得した1列の文字列を渡す
  f.close()

if __name__ == '__main__':
  args = sys.argv
  if len(args) == 2: #引数を2つ以上付ける
    search_str = sys.argv[1]
    search_file('usingjson.json', search_str)
  else:
    print('Usage$ python',args[0], 'search string')
    print('example ... $ python',args[0], 'parameter2')
    quit()

