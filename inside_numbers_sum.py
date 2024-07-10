n = [[5,6,7,4],
     [8,9,1,3],
     [2,3,4,5],
     [9,4,5,7]]

length = len(n)
for i in range(length):
    for j in range(length):
        if (i == 0 or i == length-1 or j == 0 or j == length-1) :
            continue
        else:
            print(n[i][j])
        