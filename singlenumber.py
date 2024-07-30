n = [5,5,1,1,2,4,2]
from collections import Counter
count = Counter(n)
print(count)

print(count)
most_element,most_value = count.most_common(1)[0]
print(most_element,most_value)

n = [5,5,1,1,2,4,2]
from collections import Counter
count = Counter(n)
print (count)

most_element,most_value = count.most_common(1)[0]
print(most_element,most_value)





unique_values = []
print(count.items)
for key, value in count.items():
    if value == 1:
        unique_values.append(key)
        


print(min(unique_values)) 
