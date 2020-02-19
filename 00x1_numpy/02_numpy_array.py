# -*- coding: utf-8 -*-
'''
假设一个团队里有5名学员，成绩如下表所示。
1.用NumPy统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
2.总成绩排序，得出名次进行成绩输出。
'''

import numpy as np
a = np.array([[4,3,2],[2,4,1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))

print("\npart 6 作业\n")

persontype = np.dtype({
    'names':['name', 'chinese','english','math' ],
    'formats':['S32', 'i', 'i', 'i']})
peoples = np.array([("ZhangFei",66,65,30),("GuanYu",95,85,98),
       ("ZhaoYun",93,92,96),("HuangZhong",90,88,77),
       ("DianWei",80,90,90)],dtype=persontype)
#指定的竖列
name = peoples[:]['name']
chinese = peoples[:]['chinese']
english = peoples[:]['english']
math = peoples[:]['math']
#定义函数用于显示每一排的内容
def show(name,cj):
    print('{} | {} | {} | {} | {} | {} '
          .format(name,np.mean(cj),np.min(cj),np.max(cj),np.var(cj),np.std(cj)))

print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
show("语文", chinese)
show("英语", english)
show("数学", math)

print("排名:")
#用sorted函数进行排序
ranking = sorted(peoples,key=lambda x:x[1]+x[2]+x[3], reverse=True)
print(ranking)