# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
# n = [2,3,1,1,4]
# right = 0
# length = len(n)
# last = length - 1
# for i in range(length):
#     if i > right:
#         print('false')
        
#     if n[i] + i > last:
#         right = n[i] + i
        
#     if right >= last:
#         print('true')


# def jump(n,length,last):
#     for i in range(length):
#         if n[i] + i == last:
#            return True
#     return False
        
# n =  [2,3,1,1,4]
# length = len(n)
# right = 0
# last = length - 1

# print(jump(n,length,last))
    

def jump(n,stepsize,length):
    for i in n:
        
        if stepsize < 0:
            return False
        if n[i] > stepsize:
            stepsize = i
               
        stepsize -= 1
    return True
   
n =  [3,2,1,0,4]
stepsize = 0
length = len(n)
    
print(jump(n,stepsize,length))