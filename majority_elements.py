

nums = [2,2,1,1,1,2,2]

from collections import Counter

maximum = Counter(nums)

for key, value in maximum.items():
    maxelement,maxvalues = maximum.most_common(1)[0]
print(maxelement)
    
