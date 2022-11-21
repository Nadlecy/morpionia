import random

def aiProcess(tab,playerStart):
    # l'ordi cherche des opportunités de gagner/bloquer le joueur
    # dans les diagonales
    for i in ["O  ","X  "]:
        if (tab[0][0] == i and tab[1][1] == i and tab[2][2]=="_  "):
            return [2,2]
        elif (tab[2][2] == i and tab[1][1] == i and tab[0][0]=="_  "):
            return [0,0]
        elif (tab[2][0] == i and tab[1][1] == i and tab[0][2]=="_  "):
            return [0,2]
        elif (tab[0][2] == i and tab[1][1] == i and tab[2][0]=="_  "):
            return [2,0]
        elif ((tab[2][2] == i and tab[0][0] == i) or (tab[0][2] == i and tab[0][2] == i) and tab[1][1] == "_  ") :
            return [1,1]
    # dans les verticales et horizontales
    for i in range(len(tab)):
        for u in range(len(tab[i])):
            for w in ["O  ","X  "]:
                if tab[i][u] == "_  ":
                    if (tab[i-1][u] == w and tab[i-2][u] ==w) or (tab[i][u-1] ==w and tab[i][u-2] == w):
                        return [i,u]    
    # si l'ordinateur joue en premier
    if playerStart =="n":
        if tab[0][0] == "_  ":
            return [0,0]
        elif tab[1][1] == "X  ":
            if tab[2][2] =="_  ":
                return [2,2]
            elif tab[2][2] == "O  " and tab[2,0] =="X  " and tab[0,2]=="_  " and tab[0,1]=="_  ":
                return [0,2]
            elif tab[2][2] == "O  " and tab[0,2] =="X  " and tab[2,0]=="_  " and tab[1,0]=="_  ":
                return [2,0]
        elif tab[1][1] == "_  ":
            if (tab[0][2] == "O  " or tab[2][0] == "O  ") and tab[0][2] != "X  " and tab[2][0] != "X  " and tab[2][2] != "X  ":
                return [1,1]
            elif (tab[0][2] == "O  " and tab[0][1] != "X  ") or (tab[2][0] == "O  " and tab[1][0] != "X  ") and tab[2][2] == "_  ":
                return [2,2]
            elif tab[0,2]=="_  " and tab[0,1]=="_  ":
                return [0,2]
            elif tab[2,0]=="_  " and tab[1,0]=="_  ":
                return [2,0]
        # si il n'y a pas eu de retour jusque là on a pas vraiment de stratégie
        while 1:
            # l'ordi va chercher une place au hasard jusqu'à en trouver une vide
            comAns = [random.randint(0,2),random.randint(0,2)]
            if tab[comAns[0]][comAns[1]] == "_  ":
                return comAns

    # si l'ordinateur joue en deuxième
    else: 
        if tab[1][1]=="_  ":
            return [1,1]
        elif tab[1][1] ==

g=[["_  ","_  ","_  "],["X  ","X  ","_  "],["_  ","_  ","X  "]]

t=aiProcess(g)
g[t[0]][t[1]]="0  "
print(g)
t=aiProcess(g)
g[t[0]][t[1]]="0  "
print(g)