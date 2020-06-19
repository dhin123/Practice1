dict1 = {'ravi':10,'rajnish':9,'sanjeev':15,'yash':2,'suraj':32}
print(sorted(dict1.items(), key=lambda x: x[1]))
d = {'aa': 3, 'bb': 4, 'cc': 2, 'dd': 1}
s = sorted(d.items(), key=lambda x: x[1])
print(s)
