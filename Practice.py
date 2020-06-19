from functools import reduce

w = [1,3,5,7,9,11,15,17,19]
x = w[::-1]
lst = []
k =3
for i in range(0,len(w), k):
    lst.append(x[i:i+k])

lst1 = reduce(lambda x, y : x+y, lst[::-1])
print(lst1)




