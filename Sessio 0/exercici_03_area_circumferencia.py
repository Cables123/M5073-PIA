"""
Calcula l'àrea d'una circumferència desant el seu radi en una variable.
Fes servir la llibreria math per obtenir el número PI. area=2∗pi∗radi

Documentació de la llibrería math: https://docs.python.org/3/library/math.html
Com fer servir la llibreria math: https://www.w3schools.com/python/ref_math_pi.asp
"""

# El teu codi aquí...

radio = float(input("Introdueix el radi de la circumferència: "))
import math

area = 2 * math.pi * radio

print("L'àrea de la circumferència és:", area)