from itertools import permutations
def concatenate(a):
    res = []


    comb = permutations(a,2)
    c = list(comb)

    for ele in a:
        c.append((ele,ele))
    print(c)
    for ele in c:
        st = ""
        st += str(ele[0]) + str(ele[1])
        res.append(int(st))
    print(res)
    return sum(res)

a = [23,45]
print(concatenate(a))




