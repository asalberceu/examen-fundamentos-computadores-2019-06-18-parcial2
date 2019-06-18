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


def codificar_palabra(palabra):
    """
    Función que codifica una palabra en morse.
    Parámetros:
        palabra: Una cadena con una palabra.
    Devuelve:
        El código morse correspondiente a la palabra con los bloques de código de cada letra separados por punto y coma.
    """
    palabra= ()
    separadas= palabra.split(",")
    palabra_codificada= separadas.values(morse)
    return palabra_codificada
    print(codificar("ANA"))


def decodificar_palabra(palabra):
    """
    Función que decodifica una palabra en morse.
    Parámetros:
        palabra: Es una cadena con bloques de código morse separados por el caracter ;.
    Devuelve:
        La palabra decodificada.
    """
     
    return palabra_codificada

    # A partir del diccionario morse construir otro diccionario invertido, es decir, cuyas claves sean los códigos morse y cuyos valores sean las letras asociadas.

    # Utilizar el diccionario anterior para decodificar cada bloque de código de la palabra.

    return palabra_decodificada


def codificar_mensaje(mensaje):
    """
    Función que codifica un mensaje en morse.
    Parámetros:
        mensaje: Una cadena con palabras separadas por espacios.
    Devuelve:
        El código morse correspondiente al mensaje con letras separadas por punto y coma y palabras separadas por espacio.
    """

    return mensaje_codificado


def decodificar_mensaje(palabra):
    """
    Función que decodifica un mensaje en morse.
    Parámetros:
        mensaje: Es una cadena código morse con letras separadas por punto y coma y palabras separadas por espacio.
    Devuelve:
        El mensaje decodificado.
    """

    return mensaje_decodificado



# Llamada a las funciones de prueba
print(codificar_palabra('Python')) #Debe devolver '.--.;-.--;-;....;---;-.'
print(decodificar_palabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.- .--.;-.--;-;....;---;-.'
print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON'

