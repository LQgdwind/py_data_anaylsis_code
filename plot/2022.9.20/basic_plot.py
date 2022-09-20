import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

y_gdp = np.array([9.4, 10.6, 9.6, 7.9, 7.8, 7.3, 6.9, 6.7, 6.8, 6.6])
y_1 = np.array([4, 4.3, 4.2, 4.5, 3.8, 4.1, 3.9, 3.3, 4, 3.5])
y_2 = np.array([10.3, 12.7, 10.7, 8.4, 8, 7.4, 6.2, 6.3, 5.9, 5.8])
y_3 = np.array([9.6, 9.7, 9.5, 8, 8.3, 7.8, 8.2, 7.7, 7.9, 7.6])

x = np.array([2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018])

plt.plot(x, y_gdp,
         'gx-.',
         label='GDP_growth_rate')
plt.plot(x, y_1,
         'rx-.',
         label='1_property_growth_rate')
plt.plot(x, y_2,
         'bx-.',
         label='2_property_growth_rate')
plt.plot(x, y_3,
         'kx-.',
         label='3_property_growth_rate')
plt.legend()
# 应用图例
plt.title('different_property_growth_rate')
# 设置标题
plt.xlabel('year',
           loc='right')
# x轴标题
plt.ylabel('growth_rate',
           loc='top')
# y轴标题
plt.xlim(2008, 2020)
plt.ylim(0.0, 15.0)
# 设置x轴和y轴范围
plt.xticks(x)
plt.yticks(np.linspace(start=0.0,
                       stop=15.0,
                       num=10))
# 设置x轴和y轴的刻度
plt.annotate(text='a certain point',
             xy=(2009, 4),
             color='purple',
             xytext=(2010, 5),
             fontfamily='consolas',
             fontsize=20,
             arrowprops=dict(arrowstyle="->")
             )
# plt.annotate是注释

# text属性是注释文本,
# xy是注释点的坐标 需要一个二维元组,
# color是字体颜色,
# xytext是注释文本的坐标,
# fontfamily是注释文本字体,
# fontsize是注释文本的大小,
# arrowprops是一个字典，传入arrow的属性

plt.plot(np.array([2009, 2009]), np.array([0, 4]),
         'k-.')

plt.text(2011, 14, 'text',
         size=20,
         fontfamily='consolas',
         color='red')
# 绘制文本

plt.show()
