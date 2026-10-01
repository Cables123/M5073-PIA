MATRIX_1 = [
      ["x",     "x", "x", "x", "x", "GOAL"],
      ["R",     "R", "R", "x", "x", "R"],
      ["R",     "x", "R", "x", "x", "R"],
      ["R",     "x", "R", "R", "x", "R"],
      ["R",     "x", "x", "R", "x", "R"],
      ["START", "x", "x", "R", "R", "R"]
  ]

positionx = 0
positiony = 0

for i in range(0, (len(MATRIX_1))):
    for j in range(0, (len(MATRIX_1[0]))):
        if MATRIX_1[i][j] == "START":
            print("Fila: ",i, "Columna:", j)

            #el eje y es la columa es decir
            positiony = j
            positionx = i

#print("Fila X: ",positionx, "Columna Y:", positiony)