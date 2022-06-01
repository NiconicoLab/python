#文字列から指定文字の検索を行い，指定箇所のみ抽出するプログラム
#指定文字は本プログラムでは'  ]'の固定にしている

'''
引数は検索対象の文字列
'''
def search(msg):
# 後方から検索して'..]'があるか検索．-1の時はヒットしていない
  if -1==msg.rfind('  ]'):
    print("not hit...")
    r=msg[msg.find('[')+1:msg.rfind(']')]
    print(r)
  else:
    print("hit!")
    r=msg[msg.find('[')+1:msg.rfind('  ]')]
    print(r)

if __name__ == '__main__':
  msg = 'python[c[+]+  ]'
  search(msg)
  print('------------')
  msg = 'python[c[+]+ -]'
  search(msg)