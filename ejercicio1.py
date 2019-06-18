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
    palabra = palabra.upper()
    palabra_codificada = []
    for i in palabra:
        for j,k in morse.items():
            if i == j:
                palabra_codificada.append(k)

    return palabra_codificada

#print(codificar_palabra("hola"))


def decodificar_palabra(palabra):
    """
    Función que decodifica una palabra en morse.
    Parámetros:
        palabra: Es una cadena con bloques de código morse separados por el caracter ;.
    Devuelve:
        La palabra decodificada.
    """
    
    nuevo_morse = dict((v, k) for (k, v) in morse.items())
    #print(nuevo_morse)
    nueva_palabra = palabra.split(";")
    palabra_decodificada = []

    for i in nueva_palabra:
        for clave,valor in nuevo_morse.items():
            if i == clave:
                palabra_decodificada.append(valor)

    # A partir del diccionario morse construir otro diccionario invertido, es decir, cuyas claves sean los códigos morse y cuyos valores sean las letras asociadas.

    # Utilizar el diccionario anterior para decodificar cada bloque de código de la palabra.

    return palabra_decodificada

#print(decodificar_palabra("--..;-.--"))

def codificar_mensaje(mensaje):
    """
    Función que codifica un mensaje en morse.
    Parámetros:
        mensaje: Una cadena con palabras separadas por espacios.
    Devuelve:
        El código morse correspondiente al mensaje con letras separadas por punto y coma y palabras separadas por espacio.
    """
    mensaje_nuevo = mensaje.split(' ')
    mensaje_codificado = list(map(codificar_palabra, mensaje_nuevo))

    return mensaje_codificado

#print(codificar_mensaje("Hola mundo"))

def decodificar_mensaje(mensaje):
    """
    Función que decodifica un mensaje en morse.
    Parámetros:
        mensaje: Es una cadena código morse con letras separadas por punto y coma y palabras separadas por espacio.
    Devuelve:
        El mensaje decodificado.
    """
    mensaje_nuevo = mensaje.split(' ')
    mensaje_decodificado = list(map(decodificar_palabra, mensaje_nuevo))

    return mensaje_decodificado



# Llamada a las funciones de prueba
#print(codificar_palabra('Python')) #Debe devolver '.--.;-.--;-;....;---;-.'
#print(decodificar_palabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
#print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.- .--.;-.--;-;....;---;-.'
#print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON'

