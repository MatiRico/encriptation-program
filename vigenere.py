# que los modulos se encarguen de las funciones que deben llevar a cabo, y que los inputs se hagan en el archivo principal.
# esto ayuda a que se sepa que cosa hace cada programa, los inputs son unicamente una manera de ingresar los datos requeridos.
import base64


def Encode(key, message):
    enc = []

    for i in range(len(message)):
        # ciclo for para que recorra todo el mensaje a encriptar
        key_c = key[i % len(key)]
        # esto divide el rango del largo de key por i, y convirtiendo cada letra (para eso
        # el rango del largo, para que tome de a una letra) en un codigo diferente, en este
        # caso el ASCII
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        # esto agrega cada letra convertida a ASCII a la lista vacia [enc]
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# funcion que realiza la codificacion de los mensajes


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


# funcion que realiza la decodificacion de los mensajes
# misma logica que la funcion anterior, solo que al reves


# ¿Como hacer para que se ejecuten las funciones y no los inputs unicamente?
