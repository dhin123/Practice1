# input string = aabbbccccaaa, maintain the insertion order  and output should be a2b3c4a3
from collections import OrderedDict
word = "aabbbccccaaa"
if not word:
    print(" ")
if len(word) ==1:
    print(word + "1")

i = 0


while i < len(word)-1:
    count =1
    while word[i] == word[i+1]:
        i+=1
        count +=1

        if i+1 == len(word):
            break

    print(str(word[i])+ str(count), end = "")
    i += 1



