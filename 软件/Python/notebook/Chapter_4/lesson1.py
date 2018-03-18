#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Chapter 4: Dictionary;Dict
#4.1 using dictionary
name = ['Alice','Beth','Cecil','Dee-Dee','Earl']
numbers = ['2341','9102','3158','0142','5551']
# print (numbers[name.index('Cecil')])

#4.1 dict
items = [('name','Gumby'),('age',42)]
d = dict(items)
# print(d)
d = {(1,2,3):5,(2,3,4):6}
# print(d[(1,2,3)])

people = {
	'Alice':{
		'phone':'2341',
		'addr':'Foo drive 23'
	},
	'Beth':{
		'phone':'9102',
		'addr':'Bar street 42'
	},
	'Cecil':{
		'phone':'3158',
		'addr':'Baz avenue 90'
	}
}
labels ={
	'phone':'phone numbers',
	'addr': 'address'
}
'''
name = raw_input('Name: ')
request = raw_input('%s (p) or %s (a)?'%(labels['phone'],labels['addr']))
if request == 'p':
	key = 'phone'
if request == 'a':
	key = 'addr'

if name in people:
	print "%s's %s is %s."%(name,labels[key],people[name][key])
'''