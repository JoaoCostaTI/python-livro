l = [2, [2,4,6,8,10], 9, 7, [1,2,3]]

for e in l:
    if isinstance(e, int):
        print(e)
    elif isinstance(e, list):
        for i in e:
            print(i, end=" ")
        print()