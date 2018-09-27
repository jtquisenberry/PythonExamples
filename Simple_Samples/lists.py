from collections import deque

a = 0


one = [0] * 8
print(one)
two = [one] * 4
print(two)


# Sort in place
times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
times.sort(key = lambda time: time[1])
print(times)
times.reverse()
print(times)
times.sort(key = lambda x: x[0])
print(times)



# Sorting with sorted
times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
sorted_times = sorted(times)
print("sorted_times", sorted(times))
print("sorted_times", sorted_times)



#Coercion of empty list to False
times = []
print(times == False)
if times:
    print("Yes")
if not times:
    print("No")


# Concatenation of lists, without extend.
list1 = [0,1,2,3,4]
list2 = [5,5,0,0]
print(list1 + list2)

# Operations on lists
print('Operations on lists')
list3 = [0,1,2,3,4,5]
print(min(list3))
print(max(list3))
print(sum(list3))
print(len(list3))
print(sorted(list3))
print(list(reversed(list3)))
print(list3.count(3))
print(list3.index(4))


# Work with queues deque
my_queue = deque([0,1,2,3,4,5])
#deque.extend()
my_queue.pop()
my_queue.popleft()
print('my_queue', my_queue)




list1.insert(0,6)
print(list1)
