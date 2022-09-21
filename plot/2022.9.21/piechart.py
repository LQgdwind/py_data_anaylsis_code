# 绘制饼图
# plt.pie()方法

# explode：设置各部分突出
# label:设置各部分标签，
# labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
# autopct：设置圆里面文本
# shadow：设置是否有阴影
# startangle：起始角度，默认从0开始逆时针转
# pctdistance：设置圆内文本距圆心距离
# 返回值
# l_text：圆内部文本，matplotlib.text.Text object
# p_text：圆外部文本

import numpy as np
import matplotlib.pyplot as plt

partition = np.array([55, 25, 10, 7, 3])
labels = ['complex', 'hard', 'medium', 'normal', 'simple']
colors = ['red', 'orange', 'blue', 'yellow', 'gray']
labeldistances = 0.5
explodes = [0.18, 0.14, 0.1, 0.07, 0.03]

plt.pie(partition,
        labels=labels,
        colors=colors,
        labeldistance=labeldistances,
        explode=explodes,
        # autopct="%1.1f%%",
        # pctdistance=0.4,
        shadow=True)
plt.legend(loc='best')
plt.title("test_complexity_statics",
          color='red',
          fontsize=16)
plt.show()
