lst = [16, 17, 4, 3, 6, 5, 2]
lst1 = [lst[-1]]
for i in range(len(lst)-1):
    lst2 = sorted(lst[i+1:], reverse=True)
    if lst[i] > lst2[0]:
        lst1.append(lst[i])
print(lst1)


