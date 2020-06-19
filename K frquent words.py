import collections
from collections import Counter
s = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

count = collections.Counter(s)
print(count)
candidates = count.keys()
print(candidates)
candidates.sort(key=lambda w: (-count[w], w))
print(candidates[:k])