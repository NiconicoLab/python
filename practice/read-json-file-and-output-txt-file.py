'''
引数で指定したファイルの中身を別ファイルに出力するものです
指定ファイルは本プログラムではjsonファイルに限定しています
'''

import sys

def ctrlfile(iparam, oparam):
  ifname = open(iparam, 'r')
  ofname = open(oparam, 'w')
  datalist = ifname.readlines()
  for data in datalist:
    #ofname.write(data) #readlinesで取得したdataには改行コードまで含まれている．
    ofname.write(data[0:-1]) #[0:-1]で最初と最後を指定すると，最後には改行コードは含まれないため，別途改行コードを入れる
    ofname.write('\n')
  ifname.close()
  ofname.close()
  
if __name__ == '__main__':
  args = sys.argv
  if len(args) == 2:
    fname = sys.argv[1]
    if -1!=fname.rfind('.json'): # *.jsonファイルか検索して，見つかった時
      ctrlfile(sys.argv[1], sys.argv[1].replace('json','_tmp.txt'))  # 拡張子を変えたものを出力ファイル名にする
    else:
      print('Not found json! This file in not json file.')
  else:
    print('Usage$ python',args[0],'<input file name> <output file name>')
    print('example ... $ python', args[0], 'usingjson.json')
    quit()
