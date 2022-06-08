import json

fpath = './usingjson.json' #jsonファイルのパス

try:
    with open(fpath) as f:
        jsn = json.load(f) #jsonファイル読み込み
        #print(jsn) #debug
except IndexError:
    print('not found')

# jsonファイルのparameter2のみ表示
print('--- test1 ---')
for jsn_key in jsn:
    print(jsn_key, end='')
    print('     ', end='')
    print(jsn[jsn_key]["parameter2"])

# jsonファイルのparameter3の1つ目のデータのみ表示
print('--- test2 ---')
for jsn_key in jsn:
    print(jsn_key, end='')
    print('     ', end='')
    print(jsn[jsn_key]["parameter3"][0])

# jsonファイルのparameter3の2つ目のデータのみ表示
print('--- test3 ---')
for jsn_key in jsn:
    print(jsn_key, end='')
    print('     ', end='')
    print(jsn[jsn_key]["parameter3"][1])
