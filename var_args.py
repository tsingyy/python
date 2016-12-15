# -*- coding: utf-8 -*-

def hello(greeting,*args):
    if(len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting,','.join(args)))
hello('Hi')
#result:Hi!
hello('Hi','Sarah')
#result:Hi,Sarah!
hello('Hello','Nichael','Bob','Adam')
#result:Hello,Michael,Bob,Adam!
names=('Bart','Lisa')
hello('Hello',*names)
#result:Hello,Bart,Lisa!
