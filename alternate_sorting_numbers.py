# input = 7 8 4 1 6 3
# output = 8 1 7 3 6 4


n = [7, 8, 4, 1, 6, 3]
add_elements = []

while n:
    if len(n) > 1:
        maxi = max(n)
        add_elements.append(maxi)
        n.remove(maxi)
        mini = min(n)
        add_elements.append(mini)
        n.remove(mini)
    elif len(n) == 1:
        add_elements.append(n[0])
        n.pop(0)

print(add_elements)


        
    
    