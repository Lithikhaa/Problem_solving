n = 5
for row in range(n):
  for col in range(row+1):
    print('*',end=' ')
  print()
  
  
  
n = int(input())
for row in range(n):
  for col in range(n):
    if col==0 or row==n-1 or row==col :
      print('*',end='')
    else:
      print(end=' ')
  print()