'''Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false '''

# s = 'abc'
# t = "ahxgdc"
# tot = ''
# for i in s:
#     for j in t:
#         if i == j:
#             tot += j
#         if tot == s:
#             print('True')
# print('False')
            
s = "acb"
t = "ahbgdc"


l = len(s)
c = 0
if not s :
    print('True')
for i in t :
    if i == s[c] :
        c += 1
    if c == l :
        break
print(l == c)
    
            
