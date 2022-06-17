import subprocess

print('*** start call subprocess ***')

print('===============')
print('call subprocess')
print('===============')

#fpath = 'search-str.py'
fpath1 = '../arg.py'
fpath2 = 'test1.txt'
fpath3 = 'test2.txt'

cmd = 'python ' + fpath1 + " " + fpath2  + " " + fpath3 

# 文字列で指定する場合shell=Trueを指定
# 指定しない場合はバックトレースが出力される
subprocess.call(cmd, shell=True)

print('*** finish call subprocess ***')
