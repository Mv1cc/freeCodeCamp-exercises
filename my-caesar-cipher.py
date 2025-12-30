def caesar(text, shift):
    alfabeto = 'qwertyuiopasdfghjklñzxcvbnm'
    alfabeto_cerrado = alfabeto[shift:] + alfabeto[:shift]
    alfabeto_unicode = str.maketrans(alfabeto, alfabeto_cerrado)
    texto_traducido = text.translate(alfabeto_unicode)
    print(texto_traducido)

caesar('Nebulosa', 3)
#Lo que hace el alfabeto es buscar la letra objetivo en el diccionario, y luego la cambia por la letra que esta 3 posiciones delante de ella.