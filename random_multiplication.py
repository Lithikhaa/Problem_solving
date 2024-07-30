n = [1,2,3,4,5,6]
count = []
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        count.append(n[i]*n[j])
     
print(count)
        