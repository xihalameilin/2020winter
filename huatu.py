import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
#添加图形属性

# plt.title('The statistics of face age dataset')
# plt.ylim=(50, 150)
x = [1.1, 2.1, 4.1, 6.1]
x1 = [0.9, 1.9, 3.9, 5.9]
Y1 = [87.7, 89, 92, 94.6]
Y2 = [96, 98, 98, 97.9]

fig, ax = plt.subplots()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xlabel('多糖浓度(mg/mL)')
plt.ylabel('结合率(%)')

x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(10)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
plt.xlim(0.5,6.5)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(50, 110)
#把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
#这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！


plt.bar(x1, Y1, facecolor='gray', width=0.2, label = '甘氨胆酸钠')
plt.bar(x, Y2, facecolor='black', width=0.2, label = '阳性对照')
plt.legend()
plt.show()