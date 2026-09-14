"""
Màquina expendedora
Crea un programa que simuli una màquina expenedora amb 3 opcions:
- Aigua (1 €)
- Refresc (1.5 €)
- Suc (2 €)

El programa ha de:
- Mostrar el menú.
- Demanar al client quina beguda vol.
- Demanar amb quants diners paga.
- Indicar si els diners són suficients i calcular el canvi.
"""

# El teu codi aquí...

print("Benvingut a la màquina expendedora!")

lista_maquina = {"Aigua": 1.0, "Refresc": 1.5, "Suc": 2.0}

input_beguda = input("Quina beguda vols? (Aigua, Refresc, Suc): ")

if input_beguda in lista_maquina:
    preu_beguda = lista_maquina[input_beguda]
    print(f"El preu de {input_beguda} és {preu_beguda} €.")
    
    diners = float(input("Amb quants diners pagues? "))
    
    if diners >= preu_beguda:
        canvi = diners - preu_beguda
        print(f"Compra realitzada! El teu canvi és {canvi:.2f} €.")
    else:
        print("Diners insuficients. Compra no realitzada.")