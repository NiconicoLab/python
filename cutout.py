import sys
def cutout(iparam, oparam):
  ifname = open(iparam, 'r')
  ofname = open(oparam, 'w')
  datalist = ifname.readlines()
  for data in datalist:
    if -1==data.rfind('  ]'):
      payload=data[data.find('[')+1:data.rfind(']')]
    else:
      payload=data[data.find('[')+1:data.rfind('  ]')]
    ofname.write(payload)
    ofname.write('\n')
  ifname.close()
  ofname.close()
  
if __name__ == '__main__':
  args = sys.argv
  if len(args) == 2:
    cutout(sys.argv[1], sys.argv[1].replace('md','txt')) 
  else:
    print('Usage$ python',args[0],'<input file name> <output file name>')
    quit()

