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
    palabrabuena = palabra.replace(""," ")[1:-1]
    palabra_codificada = ""
    for carac in palabrabuena:
        if carac != " " and carac.upper() in morse:
            palabra_codificada += morse[carac.upper()]
        elif carac == " ":
            palabra_codificada += ";"
    
    return palabra_codificada



print(codificar_palabra('paloma'))


def decodificar_palabra(palabra):
    """
    Función que decodifica una palabra en morse.
    Parámetros:
        palabra: Es una cadena con bloques de código morse separados por el caracter ;.
    Devuelve:
        La palabra decodificada.
    """
    new_dict = dict([(valor, clave) for clave, valor in morse.items()])
    palabra_decodificada = ""
    for carac in palabra.split(";"):
        if carac != " " and carac.upper() in new_dict:
            palabra_decodificada += new_dict[carac.upper()]

    # A partir del diccionario morse construir otro diccionario invertido, es decir, cuyas claves sean los códigos morse y cuyos valores sean las letras asociadas.

    # Utilizar el diccionario anterior para decodificar cada bloque de código de la palabra.

    return palabra_decodificada

print(decodificar_palabra('paloma'))


def codificar_mensaje(mensaje):
    """
    Función que codifica un mensaje en morse.
    Parámetros:
        mensaje: Una cadena con palabras separadas por espacios.
    Devuelve:
        El código morse correspondiente al mensaje con letras separadas por punto y coma y palabras separadas por espacio.
    """

    mensajebueno= mensaje.replace(" ","$")
    palabrabuena = mensajebueno.replace(""," ")[1:-1]
    mensaje_codificado = ""
    for carac in palabrabuena:
         if carac != " " and carac.upper() in morse:
            palabra_codificada += morse[carac.upper()]
        elif carac == " ":
            mensaje_codificado += ";"
        elif carac == '$':
            mensaje_codificado += " "

    return mensaje_codificado

print(codificar_mensaje('hola paloma'))


def decodificar_mensaje(palabra):
    """
    Función que decodifica un mensaje en morse.
    Parámetros:
        mensaje: Es una cadena código morse con letras separadas por punto y coma y palabras separadas por espacio.
    Devuelve:
        El mensaje decodificado.
    """
    qwe = dict([(valor, clave) for clave, valor in morse.items()]) 
    mensaje_decodificado = ""
    palabrabuena = palabra.split(";")
    print(palabrabuena)
    for carac in palabra:
        if carac != " " and carac in qwe:
            mensaje_decodificado += qwe[carac]
        elif carac == " ":
            mensaje_decodificado += " "

    return mensaje_decodificado

# Llamada a las funciones de prueba
print(codificar_palabra('Python')) #Debe devolver '.--.;-.--;-;....;---;-.'
print(decodificar_palabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.- .--.;-.--;-;....;---;-.'
print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON'
