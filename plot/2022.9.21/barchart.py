# 参数：
#
# x: 长条形中的横坐标点list
# left: 长条形左边沿x轴坐标list
# height: 长条形对应每个横坐标的高度值
# width: 长条形的宽度，默认值为0.8
# label: 每个数据样本对应的label，后面调用legend()函数可以显示图例
# alpha: 透明度
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=0,
                stop=1.5,
                num=4,
                endpoint=True)
y1 = np.array([20, 12, 35, 23])
y2 = np.array([16, 11, 5, 6])

plt.bar(x,
        height=y1,
        width=0.2,
        alpha=0.5,
        color='red',
        label='department1')
plt.bar(x+0.2,
        height=y2,
        width=0.2,
        alpha=0.5,
        color='green',
        label='department2')
plt.xticks(x+0.1,['2014', '2015', '2016', '2017'])
# 条形图的xticks方法第一个参数给出ticks的位置,第二个参数给出ticks是什么值
plt.legend()
plt.title('a certain company')
plt.xlabel('year',
           loc='right')
plt.ylabel('number',
           loc='top')
plt.ylim(0,50)
plt.show()
