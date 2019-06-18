morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
         'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..'}

#apartado 2
morseinvert = dict(map(reversed, morse.items()))
print(morseinvert)
def decodificar_palabra(palabra):
    letras=[]

    for i in palabra:
        letra=morseinvert[i]
        letras.append(letra)
    print(letras,end='')
    return decodificar_palabra
print(decodificar_palabra('.-.'))


#Apartado 4
def decodificar_mensaje(mensaje):
    separado=[]
    for i in mensaje:
        separado.append(i)
    for i in separado:
        mensajemorse=decodificar_palabra(i)
        print(mensajemorse)
    return mensaje_decodificado
print(decodificar_mensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.'))



