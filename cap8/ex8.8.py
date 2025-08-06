def mdc (a,b):
    if b == 0:
        return a
    return mdc(b, a%b)
def mmc(a,b):
    return abs(a*b) / mdc(a,b)
print(mmc(10,5))
print(mmc(32,24))