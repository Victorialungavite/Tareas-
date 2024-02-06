import random

PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100


ataques_jugador = (
    ("malicioso", -10, 0),
    ("placaje", 0, -35),
    ("ascuas", 0, -20),
)


ataques_oponente = (
    ("latigazo", -10, 0),
    ("placaje", 0, -35),
    ("pistola de agua", 0, -40),
)


while PS_jugador > 0 and PS_oponente > 0:
    # Ataque del jugador
    ataque_jugador = input("Ataque: ").lower()
    ataque_encontrado = False
    for nombre, mod_defensa, mod_ps in ataques_jugador:
        if ataque_jugador == nombre:
            defensa_oponente += mod_defensa
            PS_oponente += mod_ps
            ataque_encontrado = True
            break
    if not ataque_encontrado:
        print("¡Ataque inválido! Tus ataques son: malicioso, placaje y ascuas")

    ataque_oponente = random.choice(ataques_oponente)
    nombre_ataque, mod_defensa, mod_ps = ataque_oponente
    defensa_jugador += mod_defensa
    PS_jugador += mod_ps


if PS_oponente <= 0:
    print("¡Felicidades, has ganado!")
else:
    print("Lo siento, has perdido...")

