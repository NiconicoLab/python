import sys
from os.path import exists

def print_data(fname):
  print("ADDRESS  | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F")
  print("----------------------------------------------------------")
  print("00000000 |", end=' ')

  with open(fname, 'rb') as f:
    data = f.read()
  cnt=0 
  for i, x in enumerate(data, 1):
    print(f"{x:02X}",end='')
    if i%16 != 0:
      print(' ',end='')
    elif i%16 == 0:
      print(end='\n')
      cnt+=16
      str = '{:08X}'.format(cnt)
      print(str, '|', end=' ')
      
if __name__ == '__main__':
  args = sys.argv
  if len(args) == 2:
    if not exists(sys.argv[1]):
      print(sys.argv[1], "is not exist.")
      quit()
    else:
      print_data(sys.argv[1])
  else:
    print('Usage$ python',args[0], 'input file (dump target)')
    quit()

