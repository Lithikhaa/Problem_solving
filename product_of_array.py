# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# nums =[-1,1,0,-3,3]


# multiply_both = []

# for i in range(len(nums)):
#     li = nums[:i] + nums[i+1:]
#     product = 1
    
#     for num in li:
#         product *= num  # Multiply all elements in the list
    
#     multiply_both.append(product)
    
    
#     print(li)
# print(multiply_both)



nums = [-1,1,0,-3,3]
mul = []
for i in range(len(nums)):
    li = nums[:i] + nums[i+1:]
    product = 1
    # print(li)
    for j in li:
        
        product = product * j
    
    mul.append(product)
print(mul)


