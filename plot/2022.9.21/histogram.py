# 绘制直方图

# x: 作直方图所要用的数据，必须是一维数组；多维数组可以先进行扁平化再作图；必选参数；
# bins: 直方图的柱数，即要分的组数，默认为10；
# range：元组(tuple)或None；剔除较大和较小的离群值，给出全局范围；如果为None，则默认为(x.min(), x.max())；即x轴的范围；
# density：布尔值。如果为true，则返回的元组的第一个参数n将为频率而非默认的频数；
# weights：与x形状相同的权重数组；将x中的每个元素乘以对应权重值再计数；如果normed或density取值为True，则会对权重进行归一化处理。这个参数可用于绘制已合并的数据的直方图；
# cumulative：布尔值；如果为True，则计算累计频数；如果normed或density取值为True，则计算累计频率；
# bottom：数组，标量值或None；每个柱子底部相对于y=0的位置。如果是标量值，则每个柱子相对于y=0向上/向下的偏移量相同。如果是数组，则根据数组元素取值移动对应的柱子；即直方图上下便宜距离；
# histtype：{‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}；'bar’是传统的条形直方图；'barstacked’是堆叠的条形直方图；'step’是未填充的条形直方图，只有外边框；‘stepfilled’是有填充的直方图；当histtype取值为’step’或’stepfilled’，rwidth设置失效，即不能指定柱子之间的间隔，默认连接在一起；
# align：{‘left’, ‘mid’, ‘right’}；‘left’：柱子的中心位于bins的左边缘；‘mid’：柱子位于bins左右边缘之间；‘right’：柱子的中心位于bins的右边缘；
# orientation：{‘horizontal’, ‘vertical’}：如果取值为horizontal，则条形图将以y轴为基线，水平排列；简单理解为类似bar()转换成barh()，旋转90°；
# rwidth：标量值或None。柱子的宽度占bins宽的比例；
# log：布尔值。如果取值为True，则坐标轴的刻度为对数刻度；如果log为True且x是一维数组，则计数为0的取值将被剔除，仅返回非空的(frequency, bins, patches）；
# color：具体颜色，数组（元素为颜色）或None。
# label：字符串（序列）或None；有多个数据集时，用label参数做标注区分；
# stacked：布尔值。如果取值为True，则输出的图为多个数据集堆叠累计的结果；如果取值为False且histtype=‘bar’或’step’，则多个数据集的柱子并排排列；
# normed: 是否将得到的直方图向量归一化，即显示占比，默认为0，不归一化；不推荐使用，建议改用density参数；
# edgecolor: 直方图边框颜色；
# alpha: 透明度；

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(10000)
plt.hist(data,
         bins=40,
         density=True,
         facecolor='gold',
         orientation='horizontal',# horizontal表示横向
         edgecolor='black',
         alpha=0.45)
plt.title("Frequent_histogram")
plt.xlabel("dom:x",
           loc='right')
plt.ylabel("frq:y",
           loc='top')
plt.show()
