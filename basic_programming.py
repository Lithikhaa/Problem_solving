
# finding prime factor
n = 45
count = []
for i in range(2,9):  
    if n % i == 0:
        count.append(i)
        
for j in count:
    tot = n // j
    print(j,'*',tot)
       
        
#hcf
hcf = 1
n = 24
m = 54 
for i in range(1,n):
    if n % i == 0 and m % i == 0:
        hcf = i
print(hcf)


   
    
