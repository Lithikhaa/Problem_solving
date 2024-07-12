
def inputget():
    data = []
    n = int(input())
    for _ in range(n):
        
        names = input()
        splitting = names.split()
        part0 = splitting[0]
        part1 = int(splitting[1])
        part2 = splitting[2:]
        data.append((part0,part1,part2))
    return data
user_input = inputget()

print(user_input)

    
















# 3
# mani 3 ram raj guna
# ram 2 kumar kishore
# mughil 3 praveen naveen ramesh