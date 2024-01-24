import random
PS_jugador=100
PS_oponente= 100
defensa_oponente= 100
defensa_jugador=100
lista_ataques= []

while PS_jugador > 0 and PS_oponente>0:
    ataque_jugador= input ("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    lista_ataques.append (ataque_jugador)
    if ataque_jugador == "malicioso":
        defensa_oponente -= defensa_oponente -10
        if defensa_oponente < 0:
            defensa_oponente= 1
    
    elif ataque_jugador == "placaje":
        PS_oponente -=35 / (defensa_oponente/100)
    elif ataque_jugador == "ascuas":
        PS_oponente -=20
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

if PS_oponente <=0:
    print ("Felicidades, has ganado")

else:
    print ("lo siento, has perdido")  

print (f"Los ataques introducidos por el usuario son {lista_ataques}")