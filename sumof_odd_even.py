n = int(input())
m = list(str(n))
even = 0
odd = 0
for i in range(len(m)):
    m[i] = int(m[i])
    if m[i] % 2 == 0:
        even += m[i]
    else:
        odd += m[i]
print(even,odd)
        