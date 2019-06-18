# Diccionario con la codificación morse
morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
         'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..'}

#1.1
def codificar_palabra(palabra):
    """
    Función que codifica una palabra en morse.
    Parámetros:
        palabra: Una cadena con una palabra.
    Devuelve:
        El código morse correspondiente a la palabra con los bloques de código de cada letra separados por punto y coma.
    """
    
    palabra_codificada = ''
    for i in palabra:
        if i.upper() in morse:
            palabra_codificada += morse[i.upper()]
    return palabra_codificada

#1.2
def decodificar_palabra(palabra):
    """
    Función que decodifica una palabra en morse.
    Parámetros:
        palabra: Es una cadena con bloques de código morse separados por el caracter ;.
    Devuelve:
        La palabra decodificada.
    """
     
    morse_invert = dict([(value,key) for key, value in morse.items()])
    palabra_decodificada = ""
    for k in palabra.split(";"):
        if k != " " and k.upper() in morse_invert:
            palabra_decodificada += morse_invert[k.upper()]
    

    return palabra_decodificada

#1.3
def codificar_mensaje(mensaje):
    """
    Función que codifica un mensaje en morse.
    Parámetros:
        mensaje: Una cadena con palabras separadas por espacios.
    Devuelve:
        El código morse correspondiente al mensaje con letras separadas por punto y coma y palabras separadas por espacio.
    """
    for i in mensaje:
        words = list(map(codificar_palabra, mensaje))
        mensaje_codificado = words
    

    return mensaje_codificado
print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.- .--.;-.--;-;....;---;-.'
