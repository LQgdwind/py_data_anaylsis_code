# plt.fill_between(x, y1, y2, where， color, alpha)
#
# 参数：
# x: x轴坐标值，为一个list
# y1: 第一条曲线对应的函数值，为x对应的函数值list
# y2: 第二条曲线对应的函数值，为x对应的函数值list
# where: 条件表达式，用于判断某个区间内是否进行填充，如果判断为True，则进行填充，否则不填充
# color: 填充区域的颜色
# alpha: 填充区域的透明度，1表示不透明，0表示完全透明

import numpy as np
import matplotlib.pyplot as plt
import time

for i in range(-10, 20, 1):
    x = np.linspace(start=-np.pi * 2,
                    stop=np.pi * 2,
                    num=1024,
                    endpoint=True)
    y1 = np.sin(x) * 2 + 2
    y2 = np.sin(x) * 2 - 2
    plt.plot(x, y1,
             'r-.',
             label='y1=2sin(x)+2')
    plt.plot(x, y2,
             'g-',
             label='y2=2sin(x)-2')
    plt.fill_between(x=x,
                     y1=1,
                     y2=y1,
                     where=y1 > 1,
                     color='yellow',
                     alpha=0.25)
    plt.fill_between(x=x,
                     y1=1,
                     y2=y1,
                     where=y1 < 1,
                     color='blue',
                     alpha=0.25)
    plt.legend()
    plt.title('sin_functions')
    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.ylim(-5, 5)
    plt.xlabel('x',
               loc='right')
    plt.ylabel('y',
               loc='top')
    plt.xticks(np.linspace(-2 * np.pi, 2 * np.pi, 8, endpoint=True))
    plt.yticks(np.linspace(-5, 5, 10, endpoint=True))

    plt.annotate("start Listening",
                 xy=(-1 * np.pi, np.sin(-1 * np.pi) * 2 + 2),
                 xytext=(-2, 4),
                 color='black',
                 fontsize=12,
                 fontfamily='consolas',
                 arrowprops=dict(arrowstyle='->')
                 )
    plt.plot(np.array([-1 * np.pi, -1 * np.pi]), np.array([-5, np.sin(-1 * np.pi) * 2 + 2]),
             'kx-.')
    plt.plot(np.array([i*0.1*np.pi, i*0.1*np.pi]), np.array([-5, np.sin(i*0.1*np.pi)*2 + 2]),
         'kx-.')
    time.sleep(0.05)
    plt.show()

