# -*- coding: utf-8 -*-
#if-elif语句
#输入身高和体重来计算bmi,并判断体重情况
#height = 1.75
#weight = 80.5
height = float(input('please input height:'))
weight = float(input('please input weight:'))
bmi = weight/(height*height)
if bmi<=18.5:
    print('bmi=','%.2f' % bmi,'<18:xiaoming is too light')
elif bmi < 25:
    print('bmi=','%.2f' % bmi,'between18-25:xiaoming is normal')
elif bmi < 28:
    print('bmi=','%.2f' % bmi,'between25-28:xiaoming is too heavy')
elif bmi < 32:
    print('bmi=','%.2f' % bmi,'between28-32:xiaoming is fat')
else:
    print('bmi=','%.2f' % bmi,'>32:xiaoming is too fat')
