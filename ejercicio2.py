def leer_fichero(url):
    fichero = open('AdjudicacionAlquilerViviendas.csv', 'r')
    datos = fichero.readlines()
     
    for dato in fichero:
        campos = dato.split(';')
        datos_viviendas = []
        datos_viviendas.append(campos)
        #print(lista)
    f.close()
    return datos_viviendas


def distritos(datos_viviendas):
    listas = []
    listas.append(datos_viviendas)
    for listas in datos_viviendas:
        for campos[0] in datos_viviendas:
            distritos = []
            distritos.append(campos[0])

        

    return distritos


def filtrar_distritos(datos_viviendas, distritos):
    for aux in datos_viviendas:
        for i, j in campos[2:4]:
            viviendas = []
            viviendas.append(campos)

        


    return viviendas



# Llamada a las funciones de prueba
datos = leer_fichero('https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv')
print(distritos(datos))
datos_filtrados = filtrar_distritos(datos, ['CHAMBERI', 'HORTALEZA'])
print(viviendas_distritos(datos_filtrados))  #Devuelve un diccionario con el número total de viviendas arrendadas en Chamberí y Hortaleza.

