# 0,1,1,2,3,5,8,13
n = 7

a, b = 0, 1
print(a)
print(b)

for i in range(n-2):
    c = a + b
    a = b
    b = c
    print(c)