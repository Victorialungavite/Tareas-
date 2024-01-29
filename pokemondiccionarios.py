import random
PS_jugador=100
PS_oponente= 100
defensa_oponente= 100
defensa_jugador=100




while PS_jugador > 0 and PS_oponente>0:
    ataquesjugador= {}

    ataque_jugador= input ("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador == "malicioso":
        defensa_oponente -= defensa_oponente -10
        ataquesjugador ["malicioso"]=10
        print (ataquesjugador)
        if defensa_oponente < 0:
            defensa_oponente= 1

    elif ataque_jugador == "placaje":
        PS_oponente -=35 / (defensa_oponente/100)
        ataquesjugador["placaje"]= 35
        print (ataquesjugador)
    elif ataque_jugador == "ascuas":
        PS_oponente -=20
        ataquesjugador ["ascuas"]=20
        print (ataquesjugador)
    else:
        print ("Que estas haciendo!? Tuas ataques son malicioso, placaje y ascuas")

    #Turno del oponente 
    ataque_oponente = random.randrange (1,3+1)
    if ataque_oponente == 1: #latigo
        defensa_jugador -= defensa_jugador - 10
        if defensa_jugador <=0:
            defensa_jugador =1
    elif ataque_oponente == 2: #placaje
        PS_jugador -=35 / (defensa_jugador /100) 
    elif ataque_oponente ==3: #pistola de agua
        PS_jugador -= 40


print("El diccionario guardo estos ataques:")
print (ataquesjugador)
if PS_oponente <=0:
    print ("Felicidades, has ganado")

else:
    print ("lo siento, has perdido")  

