#循环

#计算十个数的和 用 for X in Y[]
'''
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+x
print('10以内的数加起来的和为',sum)
'''

#打印list
'''
names = ['JAVA','C','C#','RUBY','PYTHON','Javascript']
for name in names:
	print(name)
'''
#range()函数可以生成一个整数序列，如range(5)生成的序列是从0开始小于5的整数
#list(range(5))运行结果为[0,1,2,3,4]即为从0开始小于5的整数序列
#计算100以内数的和
sum = 0
for x in range(101):
    sum=sum+x
print('100以内数的和:',sum)
