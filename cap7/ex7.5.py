s1 = 'AATTGGAA'
s2 = 'TG'
s3 = ''

for letra in s1:
    if letra not in s2:
        s3 += letra
print(s3)