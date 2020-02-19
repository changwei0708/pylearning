
# -*- coding: utf-8 -*
#定义一个dictionary
score = {'guanyu':95,'zhangfei':96}
#添加一个元素
score['zhaoyun'] = 98
print (score)
#删除一个元素
score.pop('zhangfei')
#查看key是否存在
print ('guanyu' in score)
#查看一个key对应的值
print (score.get('guanyu'))
print (score.get('yase',99))