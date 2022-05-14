# -*- coding: utf-8 -*-

from pylab import *

# -10 から 10 まで 0.1 刻みの配列をつくる (numpy.arange )
x  = arange(-10.0, 10.0, 0.1)

# 関数 numpy.sin : x の各要素に Math.sin を適用して配列オブジェクトを生成
y1 = sin(x)
# 関数 numpy.cos : x の各要素に Math.cos を適用して配列オブジェクトを生成
y2 = cos(x)

# x,y を描画
plot(x,y1)
plot(x,y2,'r*')

#ラベルの追加
title('Figure') #タイトル
xlabel('t [ms]') # X 軸
ylabel('Out [V]') # Y 軸

# 描画
show()