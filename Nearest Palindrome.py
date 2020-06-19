from functools import reduce

x = "123456"
print(x[::-1])
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
lst = reduce(lambda x,y:x+y ,li)
print(lst)
