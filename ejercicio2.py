def leer_fichero(url):
    """
    Función que abre un fichero de texto desde una url y devuelve una lista de listas con los datos del fichero.
    Parámetros:
        url: URL del fichero de texto en formato csv donde cada registro aparece en una línea y los campos están separados por punto y coma `;`.
    Devuelve:
        Una lista cuyos elementos son a su vez listas que contienen los datos de cada línea del fichero menos la primera línea.
    """

    return datos_viviendas


def distritos(datos_viviendas):
    """
    Función recibe una lista de listas con los datos de la viviendas arrendadas y devuelve los distritos.
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
    Devuelve:
        Una lista con los distritos correspondientes a cada lista.
    """

    return distritos


def filtrar_distritos(datos_viviendas, distritos):
    """
    Función que recibe una lista de listas con los datos de las viviendas arrendadas y una lista de nombres de distritos y devuelve una lista con las listas correspondientes a los distritos indicados
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
        distritos: Una lista de cadenas con nombres de distritos.
    Devuelve:
        Una lista con las listas que contienen los datos de las viviendas arrendadas de los distritos indicados.
    """

    return datos_distritos


def viviendas_distritos(datos_viviendas):
    """
    Función que recibe una lista de listas con los datos de las viviendas arrendadas y devuelve un diccionario con los nombres de los distritos y el número total de viviendas arrendadas en el distrito.
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
    Devuelve:
        Un diccionario cuyas claves son los nombres de los distritos y cuyos valores son el número total de viviendas arrendadas en cada distrito.
    """

    return viviendas



# Llamada a las funciones de prueba
datos = leer_fichero('https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv')
print(distritos(datos))
datos_filtrados = filtrar_distritos(datos, ['CHAMBERI', 'HORTALEZA'])
print(viviendas_distritos(datos_filtrados))  #Devuelve un diccionario con el número total de viviendas arrendadas en Chamberí y Hortaleza.

