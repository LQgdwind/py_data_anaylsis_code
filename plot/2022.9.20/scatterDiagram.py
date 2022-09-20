# scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)
# 函数用于在图像中绘制散点
# 参数：
# x/y:  都是向量形式，且维度相同，分别对应坐标点的横纵坐标
# scalar:   标记大小，以平方磅为单位的标记面积，可以有一下形式：
#           数值标量 ： 以相同的大小绘制所有标记。
#           行或列向量 ： 使每个标记具有不同的大小。x、y 和 sz 中的相应元素确定每个标记的位置和面积。sz 的长度必须等于 x 和 y 的长度。
#           [] ： 使用 36 平方磅的默认面积。
# color: 标记的颜色
# marker: 标记样式
# edgecolors: 轮廓颜色，参数形式和color类似
# alpha: 透明度，值在[0, 1]范围内，1表示不透明，0表示透明
# linewidths: 线宽，表示标记边缘的宽度，默认是"face"
# cmap: 自定义色彩盘，实际上就是一个三列的矩阵，shape为[ N , 3 ] [N, 3][N,3]，一个实例可以参考matplotlib使用自己想要的color map
import random

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(loc=0,
                     scale=1,
                     size=1024)
y = np.random.normal(0, 1, 1024)
t = np.arctan2(y, x)
plt.scatter(x=x,
            y=y,
            s=75, # s是散点的大小
            c=t, # 将坐标的正切映射到颜色
            marker='*',# 散点的形状
            alpha=0.5)
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()