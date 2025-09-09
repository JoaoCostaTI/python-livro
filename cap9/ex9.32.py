import sys
import os
import os.path

open("linhaComando.txt", 'w').close()

print(sys.argv)

a = sys.argv[1]

if os.path.isdir(a):
    print('É diretório')
elif os.path.isfile(a):
    print('É arquivo')
