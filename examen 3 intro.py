#Daniela Martínez Cedeno

#Reto 1

'''entradas= la cadena de texto
salidas= la cadena de texto resultada (las minúsculas como mayúsculas y viceversa)
restricciones= debe escribir la cadena de texto como string
'''

def invertirMayusculaMinuscula(cadenaTexto):
    indice=0
    caracter=""
    resultado=""
    while (indice<len(cadenaTexto)):
        caracter=cadenaTexto[indice]
        if (caracter.isupper()==True):
            caracter=caracter.lower()
        elif (caracter.islower()==True):
            caracter=caracter.upper()
        resultado=resultado+str(caracter)
        indice+=1
    return (resultado)


#Reto 2

'''entradas= la cadena de texto, la parte que se va a buscar en la cadena de
texto y por lo que se va a reemplazar en la caden de texto.
salidas= el resultado con la nueva cadena de texto formada por la sustitución
de partes en la cadena
restricciones= debe escribir cada uno de los parámetros comos string 
'''
def buscarYReemplazar(cadenaTexto, cadenaBuscar, cadenaReemplazar):
    cantidad=len(cadenaBuscar)
    indice=0
    resultado=""
    palabra=""
    while (indice<=len(cadenaTexto)):
        palabra=cadenaTexto[0:int(palabra(cadenaTexto))+1]
        print (palabra)
        if (cadenaBuscar in palabra):
            resultado=resultado+str(cadenaReemplazar)
        else:
            resultado=resultado+str(palabra)
        indice+=1
        cadenaTexto=cadenaTexto[int(palabra(cadenaTexto)):len(cadenaTexto)-1]
    return (resultado)

def palabra(cadenaTexto):
    indice=0
    caracter=""
    resultado=""
    contar=0
    while (indice<len(cadenaTexto)):
        caracter=cadenaTexto[indice]
        if (caracter.isupper()==True or caracter.islower()==True):
            contar+=1
        elif (caracter==" "):
            return (contar)
        indice+=1

#Reto 3

'''entradas= una cadena de texto
salidas= el promedio de letras por palabra
restricciones= escribir correctamente cada signo de puntuación (debe ir junto a
la palabra que lo antecede), ingresar la cadena como string, los signos de
puntuación y valores numéricos se omiten
'''
    
def promedioLetrasPorPalabra(cadenaTexto):
    indice=0
    contar=0
    cantidad=1
    caracter=""
    while (indice<len(cadenaTexto)):
        caracter=cadenaTexto[indice]
        if (caracter.isupper()==True or caracter.islower()==True):
            contar+=1
        if (caracter==" "):
            cantidad+=1
        indice+=1
    resultado=contar//cantidad
    return (resultado)
        
            
