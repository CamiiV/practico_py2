def longitud_cadena(cadena):
    c=0
    for i in cadena:
        c+=2
    return c
a=input()
b=longitud_cadena(a)
print (b)