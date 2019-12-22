import matplotlib.animation as animation

import matplotlib.pyplot as plt

from wave_function import gen_ims

fig = plt.figure()
ims = gen_ims()

# 10枚のプロットを 100ms ごとに表示
ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save("output.gif", writer='pillow')