'''
引数で指定したファイルの中身をExcel(xlsx)に出力するものです
指定ファイルは本プログラムではjsonファイルに限定しています
'''

import sys
import openpyxl

def ctrlfile(iparam, oparam):
  ifname = open(iparam, 'r')
  # Excelの開始処理
  wb = openpyxl.Workbook()   
  ws = wb.worksheets[0] # sheetを設定
  ws.title = "sample" # sheetのタイトル名を変更

  row=1
  column=1
  cnt=1

  datalist = ifname.readlines()
  for data in datalist:
    msg=data[0:-1] #改行コードを除いた文字列を取得
    ws.cell(row, column).value = msg #Excelの指定したセルへの書き込み
    row +=1
    cnt+=1
    if cnt == 11: #10行出力した場合，次回は別の列に出力するように設定
      column +=2
      cnt=1

  ifname.close()
  # Excelの終了処理
  wb.save(oparam) # 保存
  wb.close() # 終了

if __name__ == '__main__':
  args = sys.argv
  if len(args) == 2:
    fname = sys.argv[1]
    if -1!=fname.rfind('.json'): # *.jsonファイルか検索して，見つかった時
      ctrlfile(sys.argv[1], sys.argv[1].replace('.json','_tmp.xlsx'))  # 拡張子を変えたものを出力ファイル名にする
    else:
      print('Not found json! This file in not json file.')
  else:
    print('Usage$ python',args[0],'<input file name> <output file name>')
    print('example ... $ python', args[0], 'usingjson.json')
    quit()
