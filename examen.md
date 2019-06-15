# Examen Extraordinario de Fundamentos de Computadores (Segunda parte)
Fecha: 18 de junio de 2019  
Tiempo: 1 hora y 15 minutos

## Ejercicio 1 (5 puntos)
Definir funciones para codificar y decodificar mensajes en código morse.

1. Definir una función para codificar una palabra en código morse. Debe cumplir los siguientes requisitos:

   - Debe usarse el diccionario que se da.
   - El único parámetro de entrada de la función es una cadena con una palabra.
   - Debe devolver una cadena con el código morse correspondiente a la palabra, separando los bloques de código correspondientes a cada letra por punto y coma `;`.

2. Definir una función para decodificar una palabra en código morse. Debe cumplir los siguientes requisitos:

   - A partir del diccionario que se da se debe crear el diccionario invertido, es decir, un diccionario cuyas claves son los códigos morse y sus valores las letras correspondientes. Se valorará especialmente el uso de comprensión de diccionarios.
   - El único parámetro de entrada de la función es una cadena de código morse, donde los bloques de código correspondientes a cada letra van separados por puntos y coma `;`.
   - Debe devolver una cadena con la palabra decodificada.

3. Definir una función para codificar un mensaje en código morse. Debe cumplir los siguientes requisitos:

   - Debe usarse la función anterior para codificar palabras.
   - El único parámetro de entrada de la función es una cadena con un mensaje (palabras separadas con espacios).
   - Debe devolver una cadena con las palabras del mensaje codificadas y separadas por espacios.
   - Se valorará especialmente el uso de programación funcional.

4. Definir una función para decodificar un mensaje en código morse. Debe cumplir los siguientes requisitos:

   - Debe usarse la función anterior para decodificar palabras.
   - El único parámetro de entrada de la función es una cadena con un mensaje en código morse (letras separadas por punto y coma, y palabras separadas con espacios).
   - Debe devolver una cadena con las palabras del mensaje decodificadas y separadas por espacios.
   - Se valorará especialmente el uso de programación funcional.

Nota: Abrir el fichero `ejercicio1.py` y completar las definiciones de las funciones.

## Ejercicio 2 (5 puntos)
La url `https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv` apunta a un fichero en formato csv con datos de los arrendamientos de viviendas de la Empresa Municipal de la Vivienda del Ayuntamiento de Madrid. 

1. Construir una función que abra un fichero con el formato anterior y devuelva una lista cuyos elementos son a su vez las listas que contienen los datos de cada línea del fichero menos la primera línea. Debe cumplir los siguientes requisitos:

   - La función recibirá como único parámetro la url del fichero.
   - Debe leer el fichero por líneas y para cada línea debe dividir la línea por el separador de campos (punto y coma) y guardar los datos en una lista.
   - Debe devolver la lista con las listas de datos obtenidas a partir de cada línea.

2. Construir una función que reciba una lista de listas como la que devuelve la función anterior y devuelva otra lista con los nombres de los distritos contenidos en la lista. Debe cumplir los siguientes requisitos:

    - La función recibirá como único parámetro una lista de listas con las viviendas arrendadas por distrito.
    - Debe recorrer la lista de listas y para cada lista debe extraer el nombre del distrito y añadirlo a una lista con los distritos.
    - Debe devolver la lista de distritos.

3. Construir una función que reciba una lista de listas como la que devuelve la primera función y una lista de nombres de distritos y devuelva la lista con las listas correspondientes a los distritos indicados. Debe satisfacer los siguientes requisitos:

    - La función recibirá como parámetros una lista de listas con las viviendas arrendadas por distrito y otra lista con nombres de distritos.
    - Debe recorrer la lista de viviendas arrendadas y añadir a otra lista nueva las líneas correspondientes a los distritos indicados en la segunda lista.
    - Debe devolver la nueva lista con las listas correspondientes a los distritos indicados.

4. Construir una función que reciba una lista como la que devuelve la primera función y devuelva un diccionario cuyas claves sean los nombres de distrito y cuyos valores sean el total de viviendas arrendadas en el distrito. Debe cumplir los siguientes requisitos:

    - La función recibirá como único parámetro la lista con las viviendas arrendadas por distrito.
    - Debe recorrer la lista de listas y para cada lista extraer el nombre del distrito y el total de viviendas arrendadas en el distrito y añadir el par a un diccionario.
    - Debe devolver un diccionario con un par para cada lista de la lista, cuya clave sea el nombre del distrito y cuyo valor sea el número total de viviendas arrendadas en ese distrito.

5. Puntuación extra: Construir una función que reciba una lista como la que devuelve la primera función, una lista de distritos y el nombre de un campo (columna) y devuelva la suma de las viviendas correspondientes al campo indicado para los distritos dados. Debe cumplir los siguientes requisitos:

   - La función recibirá como parámetros una lista de listas con las viviendas arrendadas por distrito, otra lista con nombres de distritos y una cadena con el nombre de un campo o columna.
   - Debe devolver la suma total de viviendas del campo en los distritos dados.

Nota: Abrir el fichero `ejercicio2.py` y completar la definición de las funciones.
