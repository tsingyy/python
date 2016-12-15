# -*- coding:utf-8 -*-
def print_scores(**kw):
    print('    Name    Score')
    print('------------------')
    for name,score in kw.items():
        print('%10s  %d' % (name,score))
    print()
#print_scores(Adam=99,Lisa=88,Bart=77)
#print name and score
data = {
    'Adam Lee':99,
    'Lisa S':88,
    'F.Bart':77
}
print_scores(**data)

def print_info(name,*,gender,city='BeiJing',age):
    print('Personal Info')
    print('--------------')
    print('    Name:%s' % name)
    print('  Gender:%s' % gender)
    print('    City:%s' % city)
    print('     Age:%s' % age)
    print()
print_info('Bob',gender='male',age=38)
print_info('Lisa',gender='female',city='Shanghai',age=22)