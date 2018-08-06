from collections import deque

a = 0

'''
one = [0] * 8
print(one)
two = [one] * 4
print(two)
'''

'''
times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
times.sort(key = lambda time: time[1])
print(times)
times.reverse()
print(times)
times.sort(key = lambda x: x[0])
print(times)
'''

'''
# Sorting with sorted
times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
sorted_times = sorted(times)
print("sorted_times", sorted(times))
print("sorted_times", sorted_times)
'''

'''
#Coercion of empty list to False
times = []
print(times == False)
if times:
    print("Yes")
if not times:
    print("No")
'''

list1 = [0,1,2,3,4]
list2 = [5,5,0,0]
print(list1 + list2)


