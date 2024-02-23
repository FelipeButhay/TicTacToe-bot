import csv

array = [0 for x in range(9)]

import os
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')
try:
    os.remove(f"{direc}/data.csv")
except:
    pass

def win(position):
    # 0 gana X, 1 gana O, 2 empate, 3 sigue en juego
    
    d = (((0,0), (1,1), (2,2)), ((2,0), (1,1), (0,2)))
    h = tuple(tuple((x,y) for y in range(3)) for x in range(3))
    v = tuple(tuple((x,y) for x in range(3)) for y in range(3))
    for i in [*d, *h, *v]:
        if position[i[0][0]][i[0][1]] == position[i[1][0]][i[1][1]] == position[i[2][0]][i[2][1]] == 1 or \
           position[i[0][0]][i[0][1]] == position[i[1][0]][i[1][1]] == position[i[2][0]][i[2][1]] == 0:
            return position[i[0][0]][i[0][1]]
    
    for x in range(3):
        for y in range(3):
            if position[x][y] == 2:
                return 3
    return 2

def minimax(arr, turn):
    wins = win([arr[:3], arr[3:6], arr[6:]])
    match wins:
        case 0:
            return -1, None
        case 1:
            return 1, None
        case 2:
            return 0, None
        case 3:
            pass
        
    values = []
    moves = []
    for x in range(9):
        if arr[x] == 2:
            arr[x] = turn
            values.append(minimax(arr, abs(turn-1))[0])
            moves.append(x)
            arr[x] = 2
            
    if turn == 0:
        return min(values), moves[values.index(min(values))]
    elif turn == 1:
        return max(values), moves[values.index(max(values))]

def recursive(depth, turn) -> None:
    if depth == 0:
        return None
    
    for z in range(3):
        array[len(array)-depth] = z
        if depth == 1:
            with open(f"{direc}\\data.csv", "a", newline="") as file:
                position_str = "".join([str(i) for i in array])
                turn_str = str(turn)
                wins_str = win([array[:3], array[3:6], array[6:]])
                if wins_str == 3:
                    csv.writer(file).writerow([position_str, turn_str, minimax(array, turn), wins_str])
                else:
                    csv.writer(file).writerow([position_str, turn_str, None, wins_str])
                
        recursive(depth - 1, abs(turn-1))
    
    return None

for x in range(2):
    recursive(9, x)
    
    