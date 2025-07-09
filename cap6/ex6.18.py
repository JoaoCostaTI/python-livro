l = [1,2,3,4,5]

for indices in range(len(l)):
    x = 0
    for elementos in range(len(l)):
        if x == len(l)-1:
            break
        elif l[x] < l[x+1]:
            temp = l[x]
            l[x] = l[x+1]
            l[x+1] = temp
        x += 1

print(l)