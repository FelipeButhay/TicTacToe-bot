import csv
import os

direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')

def main(board, turn):
    array = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == None:
                array.append(2)
            else:
                array.append(board[x][y])
                
    array = "".join([str(x) for x in array])
    
    with open(f"{direc}/newdata.csv", "r") as file:
        csv_reader = csv.reader(file)
        for x in list(csv_reader)[::2]:
            if x[0] == array and x[1] == str(turn):
                return int(x[2][1:-1].split(", ")[1])
    
    # row = df[(df["pos"] == array) & (df["turn"] == turn)]
    
    # print("Tipo de 'turn' en el DataFrame:", df["turn"].dtype)
    # print("Tipo de 'turn' que estás buscando:", type(turn))
    # print("Valores únicos en 'turn':", df["turn"].unique())
    
    # if not row.empty:
    #     return row["move"].iloc[0]
    # else:
    #     return None