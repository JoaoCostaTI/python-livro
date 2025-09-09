import os
import os.path

for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}/")
    elif os.path.isfile(a):
        print(a)



"""
print(os.listdir())
print(os.listdir("avo"))

open("moribumdo.txt", 'w').close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("moribumdo.txt")

os.makedirs("avo/pai/filho")
os.makedirs("avo/mae/filha")
os.rename("avo/pai/filho", "avo/mae/filho")

os.mkdir("velho")
os.rename("velho", "novo")


os.makedirs("avo/pai/filho")
os.makedirs("avo/mae/filha")


os.mkdir("d")
os.mkdir("e")
os.mkdir("f")
print(os.getcwd())
os.chdir("d")
print(os.getcwd())
os.chdir("../e")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("f")
print(os.getcwd())

os.chdir("a")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("b")
print(os.getcwd())
os.chdir("../c")
print(os.getcwd())
"""