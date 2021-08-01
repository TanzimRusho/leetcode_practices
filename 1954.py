neededApples = int(input())

for i in range(10000001):
    sum = 2 * i * (i+1) * (2*i + 1)    
    if neededApples <= sum:
        print(8*i)
        break 
