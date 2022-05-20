# -*- coding: utf-8 -*-

if __name__ == '__main__':
  #四則演算
  print("** 四則演算 **")
  data1 = 1
  data2 = 5
  sum  = data1 + data2
  print(data1,'+',data2,'=',sum)
  
  #文字列制御
  print("** 文字列制御 **")
  str1 = 'Python '
  str2 = 'Verison '
  str3 = '3.7.0'
  print(str1 + str2 + str3)
  
  #for文
  print("** for文 **")
  str_array = ['string1', 'string2', 'string3']
  for name in str_array:
      print(name)
  
  for name in str_array:
      if name == "string1":
          print(name)
          print('BREAK')
          break
  
  for name in str_array:
      if name == "string1":
          print('CONTINUE')
          continue
      print(name)
  
  for i in range(5):
      print(i)
  
  #if文
  print("** if文 **")
  for i in range(5):
      if i == 0:
          print(i, ':' , 'i = 0')
      elif 0 < i < 2:
          print(i, ':' , '0 < i < 1')
      else:
          print(i, ':' , 'i > 1')
  
  #while文
  print("** while文 **")
  i = 0
  while i < 5:
      print("i=", i, ':', str(i))
      i += 1
  