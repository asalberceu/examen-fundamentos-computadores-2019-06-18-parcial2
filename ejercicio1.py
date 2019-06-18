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
    palabra_codificada = ''
    for i in palabra:
        palabra_codificada += morse[i.upper()] + ';'
    return palabra_codificada


def decodificar_palabra(palabra):
    """
    Función que decodifica una palabra en morse.
    Parámetros:
        palabra: Es una cadena con bloques de código morse separados por el caracter ;.
    Devuelve:
        La palabra decodificada.
    """

    # A partir del diccionario morse construir otro diccionario invertido, es decir, cuyas claves sean los códigos morse y cuyos valores sean las letras asociadas.
    morse_invertido = {value:key for key, value in morse.items()}
    # Utilizar el diccionario anterior para decodificar cada bloque de código de la palabra.
    palabra_decodificada = ''
    for i in palabra.split(';'):
        palabra_decodificada += morse_invertido[i]
    return palabra_decodificada


def codificar_mensaje(mensaje):
    """
    Función que codifica un mensaje en morse.
    Parámetros:
        mensaje: Una cadena con palabras separadas por espacios.
    Devuelve:
        El código morse correspondiente al mensaje con letras separadas por punto y coma y palabras separadas por espacio.
    """
    mensaje_codificado = ' '
    mensaje = mensaje.split()
    palabras_codificadas = list(map(codificar_palabra, mensaje))
    return mensaje_codificado.join(palabras_codificadas)


def decodificar_mensaje(mensaje):
    """
    Función que decodifica un mensaje en morse.
    Parámetros:
        mensaje: Es una cadena código morse con letras separadas por punto y coma y palabras separadas por espacio.
    Devuelve:
        El mensaje decodificado.
    """
    mensaje_decodificado = ' '
    mensaje = mensaje.split()
    palabras_decodificadas = list(map(decodificar_palabra, mensaje))
    return mensaje_decodificado.join(palabras_decodificadas)


# Llamada a las funciones de prueba
print(codificar_palabra('Python')) #Debe devolver '.--.;-.--;-;....;---;-.;'
print(decodificar_palabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.-; .--.;-.--;-;....;---;-.'
print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON'

