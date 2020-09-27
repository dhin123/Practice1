def hashMap(queryType, query):

    dic = {}
    s =0
    for i in range(len(queryType)):
        if queryType[i] == "insert":
            dic[query[i][0]] = query[i][1]
        elif queryType[i] == "addToValue":
            for key,val in dic.items():
                dic[key] += query[i][0]
        elif queryType[i] == "addToKey":
            kv = list(dic.items())
            dic.clear()
            for k, v in kv:
                new_key = k + query[i][0]
                dic[new_key] = v
            #print(dic)

        elif queryType[i] == "get":
            if query[i][0] in dic:
                s += dic[query[i][0]]

    return s


queryType = ["insert",
 "get",
 "insert",
 "addToValue",
 "addToValue",
 "addToValue",
 "insert",
 "addToKey",
 "get",
 "insert"]


query = [[2,1],
 [2],
 [1,3],
 [-1],
 [0],
 [3],
 [4,-5],
 [3],
 [4],
 [1,1]]

print(hashMap(queryType, query))