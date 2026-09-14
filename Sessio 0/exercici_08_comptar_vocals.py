"""
Fes un programa que, donat una cadena de text (String),
imprimeixi per pantalla el número de vocals que ha trobat.
"""

# El teu codi aquí...

text = input("Introdueix un text: ")
vocal_count = 0

for char in text:
    if char.lower() in 'aeiou':
        vocal_count += 1

print(f"El text té {vocal_count} vocals.")