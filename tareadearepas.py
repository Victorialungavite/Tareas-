
harina= input("¿Cuantas tazas de harina necesitas?")
print(harina) 
harina=int(harina)
agua= input ("¿Cuantas tazas de agua necesitas?")
print (agua)
agua=int(agua)
sal= input ("¿Cuantas cucharaditas de sal necesitas?")
print (sal)
sal=int(sal)
tazadesal=sal/48
print ("En tazas esto da  ",tazadesal)
aceite=input ("¿Cuantas cucharadas de aceite necesitas?")
print (aceite)
aceite=int(aceite)
tazasadeceite=aceite/16
print("En tazas esto da ",tazasadeceite)
resultado=harina+agua+tazadesal+tazasadeceite
print("El resultado en tazas es de", resultado)
