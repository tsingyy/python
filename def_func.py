# -*- coding: utf-8 -*-
#1，输入数据的数据类型判断；
#2，如果a为0，则方程式不是二元一次方程；
#3，如果delta小于0，那么没有实数根
#如果delta为0，那么有一个实数根
#如果delta大于0，那么有两个根
import math
print('please input a:')
a=float(input())
print('Please input b:')
b=float(input())
print('Please input c:')
c=float(input())
def quadratic(a,b,c):
    if a==0:
        return print('此方程式不是二元一次方程')
    delta=b*b-4*a*c
    if delta <0:
        return print('此方程式没有实数根')
    elif delta==0:
        x1=x2=-b/(2*a)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
    return(x1,x2)
print('方程式的实数根为：',quadratic(a,b,c))