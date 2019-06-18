def leer_fichero(url):
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')

    return datos_viviendas



datos = leer_fichero('https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv')
