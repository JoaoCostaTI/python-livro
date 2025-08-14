s = "abcdef"
z = []

for l in s:
    m = l.upper()
    z.append(m)
print(z)

z = [s.upper() for s in "abdcef"]
print(z)