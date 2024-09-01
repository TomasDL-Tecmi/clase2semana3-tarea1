#------------------------------------Primero------------------------------------

matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrix3 = [[0,0,0],
           [0,0,0],
           [0,0,0]
           ]

x=0
y=0

a=0
b=0

while(True):
    suma=(matrix1[x][y]+matrix1[x][y])
    matrix3[a][b] = suma
    b +=1
    y += 1
    if b >= 3:
        b = 0
        a += 1
    if y >= 3:
        y = 0
        x +=1
    if x == 3:
        break
print(matrix3)

#------------------------------------Segundo------------------------------------

matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrix2 = [[11,12,13],
           [14,15,16],
           [17,18,19]]

matrix3 = [[0,0,0],
           [0,0,0],
           [0,0,0]
           ]

x=0
y=0
a=0
b=0

while(True):
    suma=(matrix1[x][y]*matrix1[x][y])
    matrix3[a][b] = suma
    b +=1
    y += 1
    if b >= 3:
        b = 0
        a += 1
    if y >= 3:
        y = 0
        x +=1
    if x == 3:
        break
print(matrix3)

#------------------------------------Tercero------------------------------------
matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
inverso = []

for i in range(len(matriz[0])):
    nuevafila = []
    for j in range(len(matriz)):
      
        nuevafila.append(matriz[j][i])
 
    inverso.append(nuevafila)

for fila in inverso:
    print(fila)

#------------------------------------Cuarto------------------------------------
matriz2 = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
base = [0, 0, 0, 0, 0, 0, 0, 0]

lol = int(-1)
for i in range(0, 3):
    lol +=  1
    for j in range(0, 3):
        base[lol] = base[lol] + matriz2[i][j]        
        base[lol + 3] = base[lol + 3] + matriz2[j][i]  

for i in range(0, 3):
    base[6] = base[6] + matriz2[i][i]          
    base[7] = base[7] + matriz2[i][2 - i]      

a = True
i = 0
while a and i < 7:
    if base[i] != base[i + 1]:
        part_2 = False
    i += 1

if part_2:
    print("La matriz sí es mágica.")
else:
    print("La matriz no es mágica.")