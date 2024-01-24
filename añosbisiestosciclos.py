x= int (input("Ingresa un año entre 1900 y 2199:"))
while x> 1900 or x< 2199: 
    x= int (input("Ingresa un año entre 1900 y 2199:"))
    if (x % 4 ==0 and x % 100 !=0) or x % 400==0:
        z= x - 1900 
        f= z/4 
        print ("Hay", f , "años bisiestos en", x , "años")
    else:
        print ("El año", x , "no es bisiesto")

else:
    print ("Error, el año debe ir entre 1900 y 2199")