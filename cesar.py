# este codigo debe convertir cualquier mensaje a uno encriptado, usando el metodo cesar
# C = M + [k mod |a|]
# formula para encriptar cualquier letra con el metodo de cesar
# C es la letra encriptada
# M es la letra a encriptar
# k es la cantidad de lugares que se movera entre la letra encriptada y la a encriptar
# mod |a| es el largo del alfabeto, en este caso, siempre 27 (positivo gracias a mod)

# se puede usar la misma estructura que en vigenere.py para la funcion de encriptar y desencriptar

# se puede hacer un diccionario, y que cada letra tenga un valor numerico
# luego, al desplazar el valor numerico, que imprima la letra que tiene ese valor
alfabeto = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "ñ": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

letter = str()


def Encode(word, k1):
    for letter in word:
        value_of_letter = alfabeto.get(letter)
        # print(vletter)
        coded = value_of_letter + k1
        # print(coded)
        list_of_key = list(alfabeto.keys())
        # keys a una lista
        list_of_value = list(alfabeto.values())
        # values a una lista
        position = list_of_value.index(coded)
        # transforma en index el valor coded para buscarlo en el diccionario
        coded_letter = str(list_of_key[position])
        # busca la key segun position, osea, el index de coded
        word_replaced = word.replace(letter, coded_letter)
        # reemplazo de las letras
        # el problema actual es que imprime la palabra con una sola letra cambiada, y asi hasta cambiar cada
        # una de las letras de la palabra. El problema es la impresion de la palabra. Recursion para que
        # imprima toda la palabra cambiada, quizas un while.
        print(word_replaced)


# def Encode(letter, k1):
#     kvalue = alfabeto.get(letter)
#     print(kvalue)
#     coded = k1 + kvalue
#     print(coded)
#     list_of_key = list(alfabeto.keys())
#     list_of_value = list(alfabeto.values())
#     position = list_of_value.index(coded)
#     print(list_of_key[position])


# funcion para codificar los mensajes, letra por letra


def Decode(cletter, k2):
    # paso 1 es la obtencion de cletter
    # esto ya ocurre en index.py
    # paso 2 es la obtencion de coded, que es el valor de cletter
    coded = alfabeto.get(cletter)
    print(coded)
    # paso 3, obtener kvalue
    kvalue = coded - k2
    print(kvalue)
    # paso 4, obtener el key de kvalue e imprimirlo
    list_of_key = list(alfabeto.keys())
    list_of_value = list(alfabeto.values())
    position = list_of_value.index(kvalue)
    print(list_of_key[position])
