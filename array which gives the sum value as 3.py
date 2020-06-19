#Find the series of numbers in an array which gives the sum value as 3

a = [1, 2, 3, 4, 5, 6, 3]
lst = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] +a[j] == 6:
            lst.append((a[i],a[j]))
print(lst)
