#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#dict
d = {
     'Bob':90,
	 'Jack':87,
	 'Ben':76,
	 'Tracy':99
}
print('d=',d)
print('score of Bob=',d['Bob'])
print('d[\'Jack\']=',d['Jack'])
print('d[\'Tracy\']=',d['Tracy'])
print('Ben是否在其中：',d.get('Ben',0))
print('有Rose的成绩吗？',d.get('Rose',-1))
d.pop('Ben')
print('删除Ben的数据：',d)