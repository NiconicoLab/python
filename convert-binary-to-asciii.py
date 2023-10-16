import sys
from os.path import exists

def cnv_bin_to_ascii(fname):
  fi = open(fname, 'rb')
  fo = open('test.txt', 'w')
  while True:
    data = fi.read(1)
    if len(data) == 0:
      break
    print(data.decode())
    fo.write(data.decode())
  fi.close()
  fo.close()

if __name__ == '__main__':
  if not exists(sys.argv[1]):
    print(sys.argv[1], "is not exist.")
    quit()
  else:
    cnv_bin_to_ascii(sys.argv[1])


