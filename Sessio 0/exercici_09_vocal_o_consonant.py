"""
Donada una frase:
- Si comença per vocal, retorna el número de vocals.
- Si comença per consonant, retorna el número de consonants.
- S'ha de fer servir com a mínim 1 funció.
- Cal tenir en compte si la cadena de text no comença ni per vocal ni per consonant.
"""

# El teu codi aquí...

frase = input("Introdueix una frase: ")

if frase[0].lower() in 'aeiou':
    def comptar_vocals(text):
        return sum(1 for char in text if char.lower() in 'aeiou')
    
    num_vocals = comptar_vocals(frase)
    print(f"La frase comença per vocal '{str(frase[0]).upper()}' i té {num_vocals} vocals.")
elif frase[0].lower() in 'bcdfghjklmnpqrstvwxyz':
    def comptar_consonants(text):
        return sum(1 for char in text if char.lower() in 'bcdfghjklmnpqrstvwxyz')
    
    num_consonants = comptar_consonants(frase)
    print(f"La frase comença per consonant '{str(frase[0]).upper()}' i té {num_consonants} consonants.")
else:
    print("La frase no comença ni per vocal ni per consonant.")