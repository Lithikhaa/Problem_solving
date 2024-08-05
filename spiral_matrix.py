r = 3
c = 2
matrix = []

for i in range(r):
    li = []
    for j in range(c):       
        li.append(int(input()))
    
    matrix.append(li)
    print(matrix)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end = ' ')
    print()


li = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i == 0 and j <= len(matrix)) or (i <= len(matrix) and j == 2):
            li.append(matrix[i][j])
    for k in range(len(matrix)-1,-1,-1):          #(matrix[2])-1,-1,-1)     (matrix[2])-1 -->start(8) ,-1 --> stop , -1 --> end
        if (i == 2 and k<2):
            li.append(matrix[i][k])
            
    # for l in range(len(matrix)-1):
    #     if (i == 1 and l<2):
    #         li.append(matrix[i][l])
print(li)
    
li = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i == 0 and j <= len(matrix)) or (i <= len(matrix) and j == 2):
            li.append(matrix[i][j])
    for k in range(len(matrix)-1,-1,-1):          #(matrix[2])-1,-1,-1)     (matrix[2])-1 -->start(8) ,-1 --> stop , -1 --> end
        if (i == 2 and k<2):
            li.append(matrix[i][k])
            
for l in range(len(matrix)-1):
    if  l<2:
        li.append(matrix[1][l])
print(li)
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
li = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i == 0 and j <= len(matrix)) or (i <= len(matrix) and j == len(matrix)-1):
            li.append(matrix[i][j])
    for k in range(len(matrix)-1,-1,-1):          #(matrix[2])-1,-1,-1)     (matrix[2])-1 -->start(8) ,-1 --> stop , -1 --> end
        if (i == len(matrix)-1 and k<len(matrix)-1):
            li.append(matrix[i][k])
            
for l in range(len(matrix)-1):
    if  l<len(matrix)-1:
        li.append(matrix[len(matrix)-2][l])
print(li)
    
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]