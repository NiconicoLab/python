# -*- coding: utf-8 -*-

"""
sin関数をplotし続ける
"""
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt

def pause_plot():
    fig, ax = plt.subplots(1, 1)
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.sin(x)
    # 初期化時に一度plotし，plotしたオブジェクト(list)を受け取る受け取る
    lines, = ax.plot(x, y)
    
    while True:
        # plotデータの更新
        x += 0.1
        y = np.sin(x)
        
        # 描画データを更新するときにplot関数を使うと
        # lineオブジェクトが都度増えるため，set_data()メソッドで描画データを更新
        lines.set_data(x, y)
        
        # set_data()を使うと軸とかは自動設定されず，
        # sinカーブが描画範囲から外れるためx軸の範囲は適宜更新
        ax.set_xlim((x.min(), y.max()))
        
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # そのためplt.pause(interval)を使用
        plt.pause(.01) #引数はsleepする値

if __name__ == "__main__":
    pause_plot()