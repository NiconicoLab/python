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
  print(end='\n')

def print_ascii(str):
  val=int(str,16)
  if (val < 126) and (val >= 33):
    print(chr(val),end='')
  elif val==32:
    print(chr(val),end='')
  else:
    print(chr(46),end='')

def print_data_with_ascii(fname):
  print("ADDRESS  | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |0123456789ABCDEF|")
  print("-----------------------------------------------------------------------------")
  print("00000000 |", end=' ')

  with open(fname, 'rb') as f:
    data = f.read()
  cnt=0
  str_list=[]
  for i, x in enumerate(data, 1):
    print(f"{x:02X}",end='')
    str_list.append(f"{x:02X}")
    if i%16 != 0:
      print(' ',end='')
    elif i%16 == 0:
      print(' |',end='')
      for j in range(16):
        print_ascii(str_list[j])
      print('|',end='')
      str_list=[]
      print(end='\n')
      cnt+=16
      str = '{:08X}'.format(cnt)
      print(str, '|', end=' ')
  if i%16 != 0:
    for k in range((16-i%16)*3):
      print(' ',end='')
    print('|',end='')
    for k in range(i%16):
      print_ascii(str_list[k])
    for k in range(16-i%16):
      print(' ',end='')
    print('|',end='')
  print(end='\n')

if __name__ == '__main__':
  args = sys.argv
  if len(args) == 2:
    if sys.argv[1] == '-C':
      print('Usage$ python',args[0], '[option] file')
    elif not exists(sys.argv[1]):
      print(sys.argv[1], "is not exist.")
      quit()
    else:
      print_data(sys.argv[1])
  elif len(args) == 3:
    if sys.argv[1] == '-C':
      if not exists(sys.argv[2]):
        print(sys.argv[2], "is not exist.")
        quit()
      else:
        print_data_with_ascii(sys.argv[2])
    else:
      print('Usage$ python',args[0], '[option] file')
  else:
    print('Usage$ python',args[0], '[option] file')
    quit()

