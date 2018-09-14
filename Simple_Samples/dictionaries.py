d = dict()
d = {'a':'b','b':'c'}
d['c'] = 'd'
#d.__delitem__('b')
del d['b']
print('dict', d)


s = set()
s = {'a','b','c'}
s.add('d')
print('set', s)
s.remove('b')
print('set', s)


a = [1,2,3,4,5,6,5,7,5,8,5]
del a[0] # remove the item at index 0
print('list', a)
a.remove(5) # remove the item with value 5
print('list', a)
while 5 in a: # remove all instances of value 5
    a.remove(5)
print('list', a)



d2 = dict()
d2 = {'a':6, 'b':2, 'c':3, 'd':4}
print('dict2', d2)
i = list(d2.items())
i.sort(key= lambda x: x[1])
print(i)
#i.sort()
#print('i', i)