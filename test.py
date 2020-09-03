# class Dog(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title()+" is sitting")
#
#
# import matplotlib.pyplot as plt
# x_values = list(range(1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=5)
# plt.axis([0,1100,0,1100000])
# plt.savefig('square.png', bbox_inches='tight')
#

import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

# names = ['750', '800', '850']
# x = range(len(names))
# y = [68.3, 120.0, 86.4]


fig, ax = plt.subplots()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


x_major_locator=MultipleLocator(5)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(1)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
plt.xlim(-0.5, 18)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(0, 4)
#把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
#这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！


x1 = [0,0.25,0.5,1,1.5,2]
y1 = [5.9,16.2,32,51,79.3,100]

x2=[0,2]
y2=[0.59,100]

x3 = range(33)
y3 = [0.194,
0.178,
0.194,
0.226,
0.303,
0.426,
0.401,
0.333,
0.321,
0.339,
0.339,
0.350,
0.355,
0.375,
0.403,
0.529,
1.310,
3.214,
3.214,
3.214,
3.214,
3.010,
2.339,
1.509,
1.193,
0.641,
0.718,
0.483,
0.423,
0.341,
0.188,
0.277,
0.261]


x4 = [0,1,3,5,7,9,11,13,15,17]
y4 = [
0,
3.214,
0.45,
3.214,
3.01,
0.704,
0.664,
0.429,
0.413,
3.010
]

# y2 = [97.2 , 97.4, 98.3,  98.9,99.1 ,99.6]

# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# pl.xlim(-1, 11)  # 限定横轴的范围
# pl.ylim(-1, 110)  # 限定纵轴的范围
# plt.plot(x1, y1, marker='.', mec='black', mfc='w', c='black',label=u'多糖')
# plt.plot(x1, y2, marker='^', mec='black', mfc='w', c='black',label=u'Vc')
# plt.scatter(x1, y1, marker='s', color='black')
plt.plot(x4, y4, marker='o', mec='black', mfc='black', c='black')
#plt.legend()  # 让图例生效
# plt.xticks(x1, names, rotation=45)



plt.margins(0)
plt.xlabel("管号(5ml/管)") #X轴标签
plt.ylabel("A490") #Y轴标签

plt.show()