import cesar, vigenere


cmode = str(input("choose encription mode: "))
if cmode == "vigenere":
    message = str(input("enter text to encode or decode: "))
    print(message)
    key = str(input("enter key word: "))
    print(key)
    mode = str(input("enter mode (e or d): "))
    print(mode)
    if mode == "e":
        vigenere.Encode(key, message)
        print(vigenere.Encode(key, message))
    elif mode == "d":
        vigenere.Decode(key, message)
        print(vigenere.Decode(key, message))
    Result = str()
    print(Result)
elif cmode == "cesar":
    mode = str(input("enter mode (e or d): "))
    if mode == "e":
        #letter = input("enter a letter: ")
        word = str(input("enter a word to encode: "))
        k1 = int(input("enter a key number (remember it to decode): "))
        cesar.Encode(word, k1)
    elif mode == "d":
        cletter = input("enter coded letter: ")
        k2 = int(input("enter the key number: "))
        cesar.Decode(cletter, k2)
else:
    print("Error, no ejecuta ninguno, cambiar exec?")
