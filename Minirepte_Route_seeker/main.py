def main():
    # matrix del cami
    MATRIX_1 = [
        ["x", "x", "x", "x", "x", "GOAL"],
        ["R", "R", "R", "x", "x", "R"],
        ["R", "x", "R", "x", "x", "R"],
        ["R", "x", "R", "R", "x", "R"],
        ["R", "x", "x", "R", "x", "R"],
        ["START", "x", "x", "R", "R", "R"]
    ]

    #Matri per pintar el resultat
    resultat = [
        ["0"] * 6 for _ in range(6)
    ]

    #Cami correcte
    cami = [
        [5,0], [4,0], [3,0], [2,0], [1,0],
        [1,1], [1,2], [2,2], [3,2], [3,3],
        [4,3], [5,3], [5,4], [5,5], [4,5],
        [3,5], [2,5], [1,5], [0,5]
    ]

    for pos in cami:
        f, c = pos
        resultat[f][c] = "X"

    for fila in resultat:
        print(" ".join(fila))


main()