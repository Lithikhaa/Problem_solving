# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def dup(nums):
    num_set = set()
    print(num_set)
    for n in nums:
        if n in num_set:
            return True
        num_set.add(n)
    
    return False
nums = [1,2,3,1]
print(dup(nums))