a = [10, 20, 30, 50, 75, 80]

x = 80

for i in range(len(a)):
    for j in range(len(a)-1,-1,-1):
        if a[i] + a[j] > x:
           j = j - 1
            
        elif  a[i] + a[j] < x :
            i = i + 1
            
        elif a[i] + a[j] == x:
            print(a[i],a[j])
            
a = [10, 20, 30, 50, 75, 80]
x = 80

i = 0                # Start pointer from the beginning of the list
j = len(a) - 1       # Start pointer from the end of the list

while i < j:         # Continue until the two pointers meet
    current_sum = a[i] + a[j]
    
    if current_sum == x:
        print(a[i], a[j])
        i += 1       # Move both pointers since we found a valid pair
        j -= 1
    elif current_sum < x:
        i += 1       # Move the left pointer to increase the sum
    else:
        j -= 1       # Move the right pointer to decrease the sum

    

