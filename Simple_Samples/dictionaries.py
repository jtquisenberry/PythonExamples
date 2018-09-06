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


a = [1,2,3,4,5]
del a[0] # remove the item at index 0
print('list', a)
a.remove(5) # remove the item with value 5
print('list', a)