# 関数の戻り値のテストプログラム
# 複数の戻り値を返すためには，タプルなオブジェクトを作成し実現している

def ret1func(a, b):
  return (a+b)

def ret2func(a, b):
  return (a,b)

if __name__ == '__main__':
  ret1 = ret1func(1,2)
  print(ret1)

  '''
  複数の戻り値の場合は配列で返ってくる
  '''
  ret2 = ret2func(1,2)
  print(ret2[0], ',', ret2[1])

