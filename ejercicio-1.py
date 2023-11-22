'''
Te dan un mapa de un edificio y tu tarea es contar el número de sus habitaciones. 
El tamaño del mapa es n x m cuadrados, y cada cuadrado es suelo o pared. 
Puedes caminar hacia la izquierda, derecha, arriba y abajo a través de los cuadrados del suelo.
'''

n, m = map(int, input().split())
# n :  número de filas del mapa
# m :  número de columnas del mapa

mapa = [] # matriz que representa el mapa

for _ in range(n):
    # cada fila son 'm' caracteres que describen el mapa
    fila = list(input().strip())
    mapa.append(fila)

visitado = [[False]*m for _ in range(n)]

def dfs(i, j):
    '''función de búsqueda en profundidad para marcar las habitaciones'''
    # si la posición es inválida o es una pared, no hacer nada
    if (i < 0) or (i >= n) or (j < 0) or (j >= m) or (mapa[i][j] == '#') or visitado[i][j]:
        return
    # si no es una pared, marcar la posición como visitada
    visitado[i][j] = True
    # visitar vecinos del punto
    dfs(i+1,j)  # debajo
    dfs(i-1,j)  # encima
    dfs(i,j+1)  # derecha
    dfs(i,j-1)  # izquierda


habitaciones = 0
for i in range(n):
    for j in range(m):
        if mapa[i][j] == '.' and not visitado[i][j]: # si es suelo y no ha sido visitado anteriormente
            habitaciones += 1  # es una nueva habitación
            dfs(i, j)

print(habitaciones)
