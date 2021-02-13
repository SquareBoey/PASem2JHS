hora = 0
i= 0
"""Aprednimosa implementar lo visto en las 2 clases anteriores
ademas de esa imlpementacion pues vimos el uso de ciclos infinitos y
tambien aprendi a usar esos tres apostrofes para abrir como el codigo de comentarios"""

while True:
    num = int(input("Ingresa un numero par"))
    if num % 2 == 0:
        hora += 1
    else:
        break

print("Se contaron ",hora," numeros pares consecutivos")
