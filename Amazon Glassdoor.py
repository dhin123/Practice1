import collections
import heapq
import operator
nums = [1,1,1,2,2,2,3,0,0,0]
k = 1
nums.sort()
count = collections.Counter(nums)
print(heapq.nlargest(k, count.keys(), key=count.get))
lst = [10, 9, 8, 7, 6, 5, 4, 3, 2,1 ]
print(heapq.heapify(lst))
print(lst)


stats = {'a':1000, 'd':3000, 'c': 100, 'b':3000}
max_key = max(stats, key=stats.get)
print(max_key)

lst = [1,1,2]
i=0
while i in range(3):
    lst.append(lst[-1] + lst[-2])
    i+=1
print(lst)