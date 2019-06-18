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
    diccionario = []
    for palabra in morse.items():
        
        diccionario.append(palabra)
        print(diccionario)
        for letra in palabra:
            letra = letra.split(':')
        morse.replace(',', ';')

    palabra_codificada = str(palabra)
    #palabra = palabra.lower()
    #i.rever(',', ';')
    #for letra in morse:

        #campos = letra.split('')

    return palabra_codificada


def decodificar_palabra(palabra):
    """
    Función que decodifica una palabra en morse.
    Parámetros:
        palabra: Es una cadena con bloques de código morse separados por el caracter ;.
    Devuelve:
        La palabra decodificada.

    """
    reves = []
    variable = morse.reverse()
    reves.append(variable)
    palabra_decodificada = str(palabra)
    for letra in palabra:
        letra = letra.split(':')
        morse.replace(',', ';')

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
    decodificar_palabra()
    pmesaje_codificado = str(palabra)
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
print(codificar_palabra('belen'))
print(decodificar_palabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.- .--.;-.--;-;....;---;-.'
print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON'

