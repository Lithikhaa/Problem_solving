
# #converting int into list
# # int to list converting ----> int to str['1', '2', '3', '4', '5'] and str to int['1']-->[1] and int to list[1, 2, 3, 4, 5]
n = 12345
m = list(str(n))
print(m)
for i in range (len(m)):
    m[i] = int(m[i]) # ['1'] = [1] (converting str into list)  
print(m)

print(type(m))
print(n)
print(type(n))

# #converting list into int
# # list to str 12345 and str to int m = int(m) by using this 12345
n = [1,2,3,4,5]
m = ''
for i in range(len(n)):
    m += str(n[i])
m = int(m)
print(m)
print(type(m))
    
    
# finding square root
        
n = 144
for i in range(2,n):
    if n == i ** 2:
        print(i)
# (or)       
print(int(n**0.5))

#creating array
n = [5,8,3,7,9,1]
# [8,3,7,9,1,5] output


first = n[0]
length = len(n)
n.append(first)
n.pop(0)
print(n)
# (or)
print(n[1:])
print(n[:1])
print(n[1:] + n[:1])


