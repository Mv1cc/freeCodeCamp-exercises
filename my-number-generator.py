def number_pattern(n):
    #Valida si el argumento n es un entero.
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    #Valida si el argumento n es igual o menor a 0.
    if n <= 0:
        return 'Argument must be an integer greater than 0.'
    #Lista vacia.
    numbers = []
    #Ciclo for para recorrer los valores dentro del rango 1 hasta 1+n
    for i in range(1, 1 + n):
        #Se añade el valor de i con formato de string (str) a la lista vacia
        numbers.append(str(i))
    #Junta los valores de la lista numbers dentro de un nuevo string, separados por ' ' 
    return ' '.join(numbers)

print(number_pattern(4))