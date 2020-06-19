#You are given a large amount of log files, how would you find the top 10 visited links?

a = []
ab = sorted(a)
dict1 = {x : ab.count(x) for x in ab}

