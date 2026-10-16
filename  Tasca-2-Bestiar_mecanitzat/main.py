
import random as rd
from enum import Enum

# definimos las facciones
class Faccio(Enum):
    CHIMPANZINI = 1
    LIRILI = 2
    TRALALERO = 3

# y los proyectiles
class Projectil(Enum):
    PR = (1, 80)
    PP = (3, 35)
#proyectil regular PR y proyectil perforante PP lo primero es daño y lo segundo precision

#creamos los tanques
def crear_tanc(nom, faccio):
    if faccio == Faccio.CHIMPANZINI:
        carregador = [Projectil.PR, Projectil.PP, Projectil.PP]
        blindatge = [[13, 13, 13], [7, 7, 7]]
    elif faccio == Faccio.LIRILI:
        carregador = [Projectil.PP, Projectil.PR, Projectil.PR]
        blindatge = [[13, 13, 13], [7, 7, 7]]
    else:
        carregador = [Projectil.PR, Projectil.PP]
        blindatge = [[13, 13, 13], [7, 7, 7]]

    return {
        "nom": nom,
        "faccio": faccio,
        "blindatge": blindatge,
        "carregador": carregador,
        "torn": 0
    }

# si consiguen penetrar el blindage RIP in peperoni
def viu(t):
    for fila in t["blindatge"]:
        for x in fila:
            if x < 0:
                return False
    return True

#atacamos con un ataque aleatorio que sacamos de nuestra municion con la preccision podemos calcular si impacta o no
def atacar(atk, obj):
    p = atk["carregador"][atk["torn"] % len(atk["carregador"])]
    atk["torn"] += 1

    print(f"\n> {atk['nom']} ataca {obj['nom']} con {p.name}")

    if rd.randint(1, 100) > p.value[1]:
        print("  > El proyectil falla!")
        return

    if obj["faccio"] == Faccio.LIRILI and rd.randint(1, 100) <= 20:
        print("  > Lo esquiva!")
        return

    if obj["faccio"] == Faccio.TRALALERO and rd.randint(1, 100) <= 5:
        print("  > Lo esquiva!")
        return

    f = rd.randint(0, 1)
    c = rd.randint(0, 2)
    dany = p.value[0]

    if obj["faccio"] == Faccio.CHIMPANZINI and rd.randint(1, 100) <= 20:
        dany *= 0.5
    elif obj["faccio"] == Faccio.TRALALERO and rd.randint(1, 100) <= 10:
        dany *= 0.5

    obj["blindatge"][f][c] -= dany

    print(f"  > Ataque en la posicion ({f},{c}), daño: {dany}")


def main():
    tancs = [
        crear_tanc("Chimp_A", Faccio.CHIMPANZINI),
        crear_tanc("Lirili_A", Faccio.LIRILI),
        crear_tanc("Tralala_A", Faccio.TRALALERO)
    ]

    # Dades inicials
    for t in tancs:
        print(t["nom"], t["faccio"].name, t["blindatge"])

    ultim = None
    ronda = 0

    while sum(viu(t) for t in tancs) > 1:
        actius = [t for t in tancs if viu(t)]
        possibles = [t for t in actius if t != ultim]

        atk = rd.choice(possibles)
        objectius = [t for t in actius if t != atk]
        obj = rd.choice(objectius)

        ronda += 1
        print(f"\n=== Ronda {ronda} ===")

        atacar(atk, obj)
        ultim = atk

        for t in tancs:
            #sacamos cada linea para q el usuario sepa el status cada ronda hasta que alguno gane
            if viu(t):
                print(t["nom"], "Pecho: ", t["blindatge"][0], "Inferior: ", t["blindatge"][1])
            else:
                print(t["nom"], "K.O!")

    for t in tancs:
        if viu(t):
            print("\nGuanyador:", t["nom"], t["faccio"].name)


main()

