from random import randrange

board = [[(i * 3) + j + 1 for j in range(3)] for i in range(3)]
board[1][1] = 'X'

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for raw in board:
        for i in raw:
            print(f" {i} ", end="")
        print()

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            posicion = int(input("Por favor, digite la posición en la que desea jugar: "))
            fila,columna = obtener_posicion(posicion)
            if (fila, columna) in make_list_of_free_fields(board):
                board[fila][columna] = 'O'
                break
            else:
                print("Cuadro ya ocupado. Intente de nuevo.")
        except (ValueError, IndexError):
            print("Posición inválida. Intente de nuevo.")

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    cuadros_vacios = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                cuadros_vacios.append((i,j))
    return cuadros_vacios

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
        if all(board[d][d] == sign for d in range(3)) or all(board[d][2 - d] == sign for d in range(3)):
            return True
    return False

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        fila, columna = free_fields[randrange(len(free_fields))]
        board[fila][columna] = 'X'

def obtener_posicion(numero):
    fila = (numero - 1) // 3
    columna = (numero - 1) % 3
    return fila, columna

def ganador(board):
    if victory_for(board, 'O'):
        print("¡Felicidades! Has ganado.")
    elif victory_for(board, 'X'):
        print("La máquina ha ganado. Mejor suerte la próxima vez.")
    elif not make_list_of_free_fields(board):
        print("Es un empate.")
    return

print("¡Empecemos a jugar Tic Tac Toe!")
print("La máquina ya ha hecho su movimiento inicial (el centro).")

while True:
    # 1. Motrar tablero
    display_board(board)
    
    # 2. Turno del usuario "O"
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("¡Felicidades! ¡Has ganado!")
        break # Detiene el juego
    
    # 3. Verificar empate si no hay más espacios
    if not make_list_of_free_fields(board):
        display_board(board)
        print("¡Es un empate!")
        break

    # 4. Turno de la máquina "X"
    print("Turno de la máquina...")
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("La máquina ha ganado. ¡Suerte la próxima vez!")
        break
    
    # 5. Verficar empate si no hay más espacios
    if not make_list_of_free_fields(board):
        display_board(board)
        print("¡Es un empate!")
        break
