lst = [16, 17, 4, 3, 6, 5, 2]
res = []
max_ele = lst[-1]
res.append(max_ele)
for i in range(len(lst)- 2, -1, -1):
    if lst[i] > max_ele:
        max_ele = lst[i]
        res.append(max_ele)
print(res)

