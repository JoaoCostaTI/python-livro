l = [7,4,3,12,8]
fim = 5
while fim > 1:
    trocou = False
    
    x = 0
    while x < (fim - 1):
        if l[x] > l[x+1]:
            trocou = True
            temp = l[x]
            l[x] = l[x+1]
            l[x+1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in l:
    print(e)