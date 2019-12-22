import numpy as np
import matplotlib.pyplot as plt

def gen_ims() -> list:
    ims = []
    for i in range(10):
        im = psi()
        ims.append(im)  # グラフを配列 ims に追加
    return ims

def psi():
    rand = np.random.randn(100)  # 100個の乱数を生成
    im = plt.plot(rand)  # 乱数をグラフにする
    return im
