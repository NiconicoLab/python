#文字列を複数行に渡って記載
str_tmp = 'abc' \
'def'
print(str_tmp)

#文字列結合
str_tmp = 'a'
str_tmp = str_tmp + 'b'
str_tmp = str_tmp + 'c'
print(str_tmp)

#文字列結合
str_tmp = 'a'
str_tmp += 'b'
str_tmp += 'c'
print(str_tmp)

#回数分繰り返し
str_tmp = 'a' * 5
print(str_tmp)

#文字列への変換
str_tmp = 123
print(str(str_tmp) + 'abc')

#文字列の置換
str_tmp = '12345'
print(str_tmp.replace('123', 'abc'))

#文字列の分割
str_tmp = '123-abc'
print(str_tmp.split('-'))

#文字列の桁揃え
str_tmp = 'a'
print(str_tmp.rjust(5, '0'))
print(str_tmp.rjust(5, '!'))

str_tmp = 'abc'
print(str_tmp.zfill(5))
print(str_tmp.zfill(3))

#文字列の検索
str_tmp = '123abc'
print(str_tmp.startswith('123'))
print(str_tmp.startswith('cde'))

str_tmp = '123abc'
print('123' in str_tmp)
print('cde' in str_tmp)

#大文字/小文字変換
str_tmp = '123abcDEF'
print(str_tmp.upper())
print(str_tmp.lower())

#先頭から空白/指定文字を削除
str_tmp = '     123abc'
str_tmp = str_tmp.lstrip()
print(str_tmp)
str_tmp = str_tmp.lstrip('123') 
print(str_tmp)

#末尾から空白/指定文字を削除
str_tmp = '123abcDEF     '
str_tmp = str_tmp.rstrip()
print(str_tmp + '/')
str_tmp = str_tmp.rstrip("DEF")
print(str_tmp)

