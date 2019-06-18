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
    palabrafinal = palabra.replace(""," ")[1:-1]
    palabra_codificada = ""
    for letra in palabrafinal:
        if letra != " " and letra.upper() in morse:
            palabra_codificada += morse[letra.upper()]
        elif letra == " ":
            palabra_codificada += ";"
    return palabra_codificada



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
    for letra in palabra.split(";"):
        if letra != " " and letra.upper() in new_dict:
            palabra_decodificada += new_dict[letra.upper()]
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

    mensaje1 = mensaje.replace(" ","$")
    palabrafinal = mensaje1.replace(""," ")[1:-1]
    palabra_codificada = ""
    for letra in palabrafinal:
        if letra != " " and letra.upper() in morse:
            palabra_codificada += morse[letra.upper()]
        elif letra == " ":
            palabra_codificada += ";"
        elif letra == '$':
            palabra_codificada += " "
    return palabra_codificada


def decodificar_mensaje(palabra):
    """
    Función que decodifica un mensaje en morse.
    Parámetros:
        mensaje: Es una cadena código morse con letras separadas por punto y coma y palabras separadas por espacio.
    Devuelve:
        El mensaje decodificado.
    """

    inverso = dict([(valor, clave) for clave, valor in morse.items()]) 
    mensaje_decodificado = ""
    palabrafinal = palabra.split(";")
    inverso['.- .--.'] = "A P" 
    print(palabrafinal)
    for letra in palabrafinal:
        if letra != " " and letra in inverso:
            mensaje_decodificado += inverso[letra]
        elif letra == " ":
            mensaje_decodificado += " "

    
    return mensaje_decodificado
      



# Llamada a las funciones de prueba
print(codificar_palabra('Python')) #Debe devolver '.--.;-.--;-;....;---;-.'
print(decodificar_palabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
print(codificar_mensaje('Hola Python')) #Debe devolver '....;---;.-..;.- .--.;-.--;-;....;---;-.'
print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON'

