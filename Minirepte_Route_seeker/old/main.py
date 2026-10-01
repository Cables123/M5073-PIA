def main():

  # Possibles moviments que pot fer l'usuari
  MOVEMENTS = [
      [1,0],      # Baixar
      [-1, 0],    # Pujar
      [0, 1],     # Dreta
      [0, -1]     # Esquerre
  ]

  # Matriu quadrada que determina com serà el camí
  #    x = Cel·la bloquejada
  #    R = (Route) Cel·la desbloquejada
  #    START = Cel·la inicial
  #    GOAL = Cel·la objectiu
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

  moviment_anterior = []

  print(MATRIX_1[0][0])
  while MATRIX_1[positionx][positiony] != "GOAL":
    if pot_moure(positionx, positiony, int(6) , MOVEMENTS, moviment_anterior) == True:
      print("si")




def pot_moure(posicio_x: int, posicio_y: int, matrix_size: int, moviment: list[int], moviment_anterior: list[int]) -> bool:
  """
  Reb per paràmetres un seguit de paràmetres que, després d'un seguit de condicions, retorna True si el moviment és viable o False si no ho és

    Parameters
    ----------
    position_x : int
      Posicio actual en l'eix de les X (Columnes)

    position_y : int
      Posicio actual en l'eix de les Y (Files)

    matrix_size : int
      Mida de la matriu quadrada

    movement : list[int] (array)
      Matriu que expressa el moviment que s'ha de realitzar

    moviment_anterior: list[int] (array)
      Matriu que indica quina és la posició anterior que s'ha realitzat

  """


  # TODO: Desenvolupa el teu codi aqui...
  for mov in range(len(moviment)):
    print(mov)
  
  return True


main()