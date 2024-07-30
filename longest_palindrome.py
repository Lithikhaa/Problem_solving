s = "babad"
# ba
# bab
# baba
# babad


reversing = []
for i in range(len(s)):
    for j in range(i+1,len(s)):
        store = s[i:j+1]
        print(store)
        if store == store[::-1]:
            reversing.append(store)
print(f'Input: {s}' ,'\nOutput' ,reversing)
            
            
            