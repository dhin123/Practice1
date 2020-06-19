lst1 = [2,3,1]
lst2 = [5,4,6]
newlst = []
i = 0
newlst1 = sorted(lst1)
newlst2 = sorted(lst2)
while i in range(len(newlst1)):
    for j in range(len(newlst2)):
        newlst += [[newlst1[i], newlst2[j]]]
        i += 1
print(newlst)
