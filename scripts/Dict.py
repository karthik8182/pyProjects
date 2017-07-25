#! usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict.keys()
print dict.values()

t1 = (2,3,4,5,6,7,8,9,10,11,12,13)
print t1 [::-1]

sliceobj = slice(2,10,2)

print t1[sliceobj]

