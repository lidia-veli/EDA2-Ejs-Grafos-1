'''
Te dan un lab de un laberinto y tu tarea es encontrar un camino de principio a fin. 
Puedes caminar hacia la izquierda, derecha, arriba y abajo.
'''

# FUNCIONES que vamos a usar -------------------------------------------------------------

mov_fil = [1, -1, 0, 0]  # movimiento en la fila
mov_col = [0, 0, -1, 1]  # movimiento en la columna
movimientos = ['D', 'U', 'L', 'R']  # todos los posibles movimientos

visited = []  # nodos visitados
cola = []

def bfs(lab, inicio, final):
    '''función de búsqueda en anchura (BFS) para encontrar el camino más corto entre dos nodos
    INPUT:
    - lab: matriz que representa el laberinto
    - inicio: tupla (fila, columna) con la posición inicial
    - final: tupla (f, c) con la posición final

    OUTPUT:
    - encontrado: booleano que indica si se ha encontrado el camino
    - num_movimientos: longitud del camino recorrido hasta llegar a la casilla final
    - ruta: string con el camino recorrido hasta llegar a la casilla final
    '''
    # empezamos en la casilla de inicio
    visited.append(inicio)
    cola.append((inicio, '')) # tupla (nodo, camino seguido)

    while cola:
        # sacamos el primer nodo de la cola
        nodo, camino = cola.pop(0) # nodo es una tupla (fila, columna)
        if nodo == final:  # si es el final, hemos terminado
            return True, len(camino), camino
        
        # si no, añadimos los vecinos a la cola
        for i in range(4):
            fil = nodo[0] + mov_fil[i]  # movemos por fila
            col = nodo[1] + mov_col[i]  # movemos por columna
            # no nos salimos del laberinto, no es una pared y no hemos visitado el nodo previamente
            if (0 <= fil < n) and (0 <= col < m) and ( lab[fil][col] != '#' ) and ( (fil, col) not in visited ):
                visited.append((fil, col))
                cola.append(((fil, col), camino + movimientos[i]))
    
    # si no hemos encontrado el final, devolvemos False
    return False, 0, ''



# CODIGO EJECUTABLE ----------------------------------------------------------------------

n, m = map(int, input().split())
lab = [list(input().strip()) for _ in range(n)]

# buscamos las casillas de inicio y fin
for i in range(n):
    for j in range(m):
        if lab[i][j] == 'A':
            inicio = (i, j)
        elif lab[i][j] == 'B':
            final = (i, j)

encontrado, num_movimientos, ruta = bfs(lab, inicio, final)

if encontrado:
    print("SÍ")
    print(num_movimientos)
    print(ruta)
else:
    print("NO")
