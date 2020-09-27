from collections import OrderedDict,Counter
#exact match: input = get, output = get
#any char match: input = g?t, output = get, got, gut
#any no. of char match: input = g*t, output = get, got, gut, goat, guilt
def pattern(words, patter):
    res = []
    pat_dic = OrderedDict(Counter(patter))
    print(pat_dic)

    for word in words:
        wo_dic = OrderedDict(Counter(word))
        if wo_dic == pat_dic:
            res.append(word)
        elif "?" in patter:
            if word[0] == patter[0] and word[-1] == patter[-1]:
                if len(pat_dic) == len(wo_dic):
                    res.append(word)
        elif "*" in patter:
            if word[0] == patter[0] and word[-1] == patter[-1]:
                if len(pat_dic) <= len(wo_dic):
                    res.append(word)
    return res






patter = "g*t"
words = ["get", "got", "gut", "goat", "guilt","gotten"]
print(pattern(words,patter))
