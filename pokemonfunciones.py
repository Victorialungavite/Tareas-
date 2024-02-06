import random


def obtener_eleccion_jugador():
    ataque_jugador = input("Ataque: ").lower()
    while not ataque_jugador in ("malicioso", "placaje", "ascuas"):
        print("¡Ataque inválido! Tus ataques son: malicioso, placaje y ascuas")
        ataque_jugador = input("Ataque: ").lower()
    return ataque_jugador


def aplicar_ataque_jugador(ataque):
    global defensa_oponente, PS_oponente, lista_ataques
    for nombre, mod_defensa, mod_ps in ataques_jugador:
        if ataque == nombre:
            defensa_oponente += mod_defensa
            PS_oponente += mod_ps
            lista_ataques.append(ataque)
            break


def obtener_ataque_oponente():
    return random.choice(ataques_oponente)


def aplicar_ataque_oponente(ataque):
    global defensa_jugador, PS_jugador
    for nombre, mod_defensa, mod_ps in ataques_oponente:
        if ataque == nombre:
            defensa_jugador += mod_defensa
            PS_jugador += mod_ps
            break


def mostrar_resultado():
    if PS_oponente <= 0:
        print("¡Felicidades, has ganado!")
    else:
        print("Lo siento, has perdido...")


def mostrar_lista_ataques():
    print(f"Los ataques introducidos por el usuario son: {lista_ataques}")


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
    
    ataque_jugador = obtener_eleccion_jugador()
    aplicar_ataque_jugador(ataque_jugador)

    
    ataque_oponente = obtener_ataque_oponente()
    aplicar_ataque_oponente(ataque_oponente)

# Mostrar el resultado del combate y la lista de ataques
mostrar_resultado()
