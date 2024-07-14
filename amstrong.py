import math
import time
start  = time.time()

n = int(input())
count = 0
li = list(map(int,input().split()))
for i in li:
  count += pow(i,n)
print(count)
if count == int("".join(map(str, li))):
  print('amstrong')
else:
  print('not amstrong')
end = time.time()
print((end-start) * 10**3, "ms")