def pin_extractor(poems):
    #Crea una lista vacia para almacenar los pines
    secret_codes = []
    #Un loop for para acceder a cada poema dentro del argumento poemas
    for poem in poems:
        #Crea la variable secret_code con un string vacio para almacenar los pins individuales de cada poema
        secret_code = ''
        #Divide los poemas por linea y los almacena en una lista nueva, se le asigna el caracter especial \n para separarlos con un salto de linea
        lines = poem.split('\n')
        #Un bucle for para acceder a cada indice y cada linea, dentro de la lista lines, que a su vez esta convertida en un par de objetos iterables por el metodo enumerate()
        for line_idx, line in enumerate(lines):
            #Se guarda cada linea por separado dentro de una lista nueva creada por el metodo split, en la variable words
            words = line.split()
            #Se añade una condicional que dice que si el largo de la lista words es mayor al valor del indice de esa linea, se cumple la condicional
            if len(words) > line_idx:
                #Se añade el largo de la palabra que esta en el indice de la linea correspondiente a la variable con el string vacio, transformado a string
                secret_code += str(len(words[line_idx]))
                #Si la condicional no se cumple, es decir si el indice de la linea no existe, se añade un 0 a la variable con el string vacio
            else:
                #Añade el valor de la variable secret_code, al final de la variable con una lista vacia llamada secret_codes
                secret_code += '0'
        #Retorna el valor de secret_codes
        secret_codes.append(secret_code)
    return secret_codes


poem = 'Como un pájaro de fuego\n la luna está entre las ramas del enebro'
poem2 = 'La luna me esta mirando\nes una noche muy bella\ny yo suspiro cantando\nsolo para que mire ella'
poem3 = '''
La primavera ha venido
nadie sabe como ha sido
ha despertado la rama
y el almendro ha florecido
'''

print(pin_extractor([poem, poem2, poem3]))