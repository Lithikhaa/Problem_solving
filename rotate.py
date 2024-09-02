# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
k = 3
# k = k % len(n)
# # r = len(n) - k
# # new = n[0:r]
# # n[0:r] = []
# # print(n.extend(new))
# n[:] = n[k:] + n[:k]
k = k % len(nums)
print(k)
print(len(nums))
n = len(nums)-k
print(n)
print(nums[n:])
print(nums[:n])
nums[:] = nums[n:]+nums[:n]

print(nums)

