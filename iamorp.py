# si l'ia joue en premier
    # alors
# sinon

def triTri(tab):
    for i in range(len(tab)):
        for u in range(len(tab[i])):
            if tab[i][u] == "_  ":
                if (tab[i-1][u] == "X  " and tab[i-2][u] =="X  ") or (tab[i][u-1] =="X  " and tab[i][u-2] == "X  "):
                    tab[i][u]="O  "

g=[["_  ","_  ","_  "],["X  ","X  ","_  "],["_  ","_  ","X  "]]

triTri(g)
print(g)