
def triTri(tab):
    if tab[0][0] == "X  " and tab[1][1] == "X  " and tab[2][2]=="_  ":
        tab[2][2] = "O  "
    elif tab[2][2] == "X  " and tab[1][1] == "X  " and tab[0][0]=="_  ":
        tab[0][0] = "O  "
    elif tab[2][0] == "X  " and tab[1][1] == "X  " and tab[0][2]=="_  ":
        tab[0][2] = "O  "
    elif tab[0][2] == "X  " and tab[1][1] == "X  " and tab[2][0]=="_  ":
        tab[2][0] = "O  "
    elif (((tab[2][2] == "X  " and tab[0][0] == "X  ") or (tab[0][2] == "X  " and tab[0][2] == "X  ")) and tab[1][1] == "_  ") :
        tab[1][1] = "O  "
    else:
        for i in range(len(tab)):
            for u in range(len(tab[i])):
                if tab[i][u] == "_  ":
                    if (tab[i-1][u] == "X  " and tab[i-2][u] =="X  ") or (tab[i][u-1] =="X  " and tab[i][u-2] == "X  "):
                        tab[i][u]="O  "

g=[["_  ","_  ","_  "],["X  ","X  ","_  "],["_  ","_  ","X  "]]

triTri(g)
print(g)
triTri(g)
print(g)