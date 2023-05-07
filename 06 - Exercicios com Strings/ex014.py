def leet(palavra):
    leetspeak = {
        'a': '@',
        'b': '8',
        'c': '(',
        'd': '|)',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '|-|',
        'i': '!',
        'j': '_|',
        'k': '|<',
        'l': '1',
        'm': '|\/|',
        'n': '|\|',
        'o': '0',
        'p': '|2',
        'q': '9',
        'r': '|?',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '\/',
        'w': '|/\|',
        'x': '><',
        'y': '`/',
        'z': '2'
    }
    
    result = ""
    
    for letra in palavra:
        if letra.lower() in leetspeak:
            result += leetspeak[letra.lower()]
        else:
            result += letra
    
    return result

palavra = str(input("Informe uma palvra: "))
palavra_leet = leet(palavra)

print(f"""
A palavra: {palavra}
Leet Spek: {palavra_leet}""")
