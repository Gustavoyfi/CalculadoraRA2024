matriz= [[1,2,3], [4,5,6], [7,8,9]]
for i in matriz:
    for c in range(0,2):
        matriz[i].append(matriz[i][c])

A = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][3]) + (matriz[0][2] * matriz[1][3] * matriz[2][4])
B = 