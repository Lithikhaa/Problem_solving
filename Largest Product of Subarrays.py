nums = [2, 3, -2, 4]
multiply_both = []
for i in range(0,len(nums),2):
  multiply_both.append(nums[i]*nums[i+1])
print(multiply_both)


nums = [2, 3, -2, 4,5]
count = []
for i in range(0,len(nums)):
    for j in range(1,len(nums)-1):
        count.append(nums[i]*nums[j])
print(count)



def parition(nums):
    count = []
    
    for i in range(len(nums)-1):
        count.append(nums[i]*nums[i+1])
    print(count)
    maximum = max(count)
    print(f'The array {nums}','Output: ' ,maximum)
    
nums =   [-2, -3, 0, -2, -40]
parition(nums)

def parition(nums):   
    
    for i in range(0,len(nums),2):
        
        multiply_both.append(nums[i]*nums[i+1])
    print(multiply_both)
nums =  [-2, -3, 0, -2, -40]
multiply_both = []
for i in range(len(nums)):
    li = nums[:i]+nums[i+1:]
    parition(li)

nums = [-2, -3, 0, -2, -40]
multiply_both = []

for i in range(len(nums)):
    li = nums[:i] + nums[i+1:]
    print(li)
    
    for j in range(0, len(li) - 1, 2):
        multiply_both.append(li[j] * li[j+1])
        

print(max(multiply_both))

nums = [2, -5, -2, -4, 3]

l = 0
r = 1

li = []
for i in range(len(nums)-1):
    li.append(nums[l]*nums[r])
    l+=1
    r+=1
print(max(li))
print(li)

multiply_both = []


for i in range(len(nums)):
    li = nums[:i] + nums[i+1:]
    
    current_product = li[0]
    multiply_both.append(current_product)
    
    for j in range(1, len(li)):
        current_product *= li[j]
        multiply_both.append(current_product)


print(multiply_both)
print(max(multiply_both))





nums = [-2, -3, 0, -2, -40]
multiply_both = []


for i in range(len(nums)):
    current_product = nums[i]
    multiply_both.append(current_product)
    for j in range(i + 1, len(nums)):
        current_product *= nums[j]
        multiply_both.append(current_product)


print(multiply_both)
print(max(multiply_both))
