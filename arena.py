lista = [7,6,4,3,2]

x = len(lista)

for algo in range(len(lista)):
    i = 0
    for c in range(x):
        if i == x-1:
            break
        elif lista[i] > lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
        i += 1
print(lista)


- Laboratório 4 temos: 
    - 21 licenças com (Revit, Civil 3d, Navisworks)
- Laboratório 5
    - 21 Licenças com (AutoCad)
- Laboratório BIM
    - 2 Licença com (Auto Cad) 
- Computador competidora Worldskills
    - 1 Licença (AutoCad, Revit, NavisWorks)
