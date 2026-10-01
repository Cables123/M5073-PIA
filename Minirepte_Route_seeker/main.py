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


  camino = [[5, 0],[4,0 ],[3,0],[2,0],[1, 0],[1, 1],[1,2],[2,2],[3,2],[4,3],[]]

main()