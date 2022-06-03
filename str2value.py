
'''
文字列から数値への変換
'''
str = '11'
n10 = int(str, 10)  # 文字列を10進として数値に変換
n16 = int(str, 16)  # 文字列を16進として数値に変換

print('Convert string to value')
print(n10, end=',')
print(n16)

'''
数値から文字列への変換
'''

val = 255
str2   = format(val, 'b') # 数値を2進として文字列に変換
str8   = format(val, 'o') # 数値を8進として文字列に変換
str10 = format(val, 'd') # 数値を10進として文字列に変換
str16 = format(val, 'X') # 数値を16進として文字列に変換

print('Convert value to string')
print(str2, end=',')
print(str8, end=',')
print(str10, end=',')
print(str16)

'''
文字列から指定文字数だけを数値への変換
'''

str = 'ABCD'
s1   = str[0:1] # 開始1文字目のみ
s2   = str[1:2] # 開始2文字目のみ
s02 = str[0:2] # 開始2文字分のみ
s22 = str[2:4] # 開始2文目から4文字目まで

print('Cutout string')
print(s1, end=',')
print(s2, end=',')
print(s02, end=',')
print(s22)

