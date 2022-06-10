import sys

def cutout(argv1, argv2):
  print(argv1)
  print(argv2)
  
if __name__ == '__main__':
  args = sys.argv
  if len(args) == 3: #引数を2つ以上付ける
    cutout(sys.argv[1], sys.argv[2]) 
    #拡張子をmdからtxtへ変更する場合はsys.argv[2].replace('md','txt')のように書く
  else:
    print('Usage$ python',args[0], '...')
    quit()

