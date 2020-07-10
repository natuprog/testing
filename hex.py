import math as m

def hex (hexa):
        

print("Write the color in hex: ")
mensaje=input()
hexa=''
if (mensaje[0] == '#'):
    if (len(mensaje) == 7):
        i=0;
        while (i < 6):
            hexa[0] = mensaje[1+i]
            hexa[1] = mensaje[2+i]

ppp = 0