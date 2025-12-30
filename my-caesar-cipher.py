def caesar(text, shift):
    alfabeto = 'qwertyuiopasdfghjklñzxcvbnm' #Alfabeto a utilizar para la traduccion de los caracteres
    alfabeto_cerrado = alfabeto[shift:] + alfabeto[:shift] # Se 'Divide' el alfabeto o diccionario a usar, para cerrar el ciclo, es decir, al llegar al final del diccionario, se vuelve al principio del mismo.
    alfabeto_unicode = str.maketrans(alfabeto, alfabeto_cerrado)# Se crea la tabla traducida con los valores unicode, aun sin pasar por el translate que reemplazara los valores.
    texto_traducido = text.translate(alfabeto_unicode) # Se crea la tabla ya encriptada, con los valores reemplazados siguiendo las instrucciones dada por la tabla unicode que usa la funcion translate().
    print(texto_traducido)

caesar('Nebulosa', 3)
#Lo que hace el alfabeto es buscar la letra objetivo en el diccionario, y luego la cambia por la letra que esta 3 posiciones delante de ella.