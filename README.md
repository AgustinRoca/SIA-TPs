# Trabajo Práctico 1 - Métodos de búsqueda Desinformados e Informados con Sokoban

## Alumnos:
- Britos, Nicolás - 59.529
- Griggio, Juan - 59.092
- Roca, Agustín - 59.160

## Requerimientos:
- Python 3

## Configuración de parámetros
Se debe editar el archivo config.txt de la siguiente forma:

    1. consider_deadlock=True/False: decide si se expanden los hijos de los estados desde los cuales es imposible ganar
    2. verbose=True/False: decide si se muestra información adicional por consola
    3. algorithm=1/2/3/4/5/6: decide el algoritmo a utilizar, siendo:
        1. BFS
        2. DFS
        3. IDDFS
        4. GGS
        5. A*
        6. IDA*
    4. heuristic=1/2/3: decide la heurística a utilizar en caso de que se use un algoritmo informado, siendo:
        1. Menor suma de las distancias de cada caja a un objetivo distinto no ocupado
        2. Suma de las distancias de cada caja a su objetivo más cercano no ocupado
        3. Suma de las distancias de cada caja a su objetivo más cercano no ocupado y la distancia del jugador a la caja más cercana
    5. limit=XX: límite inicial para el IDDFS
    6. increment=XX: incremento para el IDDFS

Ejemplo de config.txt:

    consider_deadlock=True
    verbose=False
    algorithm=1
    heuristic=1
    limit=50
    increment=20

## Configuración del tablero
Se debe editar el archivo board.txt de la siguiente forma:

    ‘ ‘ (espacio en blanco): lugar libre
    ‘#’ (numeral): pared
    ‘$’ (signo pesos): caja
    ‘*’ (asterisco): objetivo con caja 
    ‘.’ (punto): objetivo sin caja
    ‘@’ (arroba): jugador

Ejemplo de board.txt:

          ###
          #.#
      #####.#####
     ##         ##
    ##  # # # #  ##
    #  ##     ##  #
    # ##  # #  ## #
    #     $@$     #
    ####  ###  ####
       #### ####

## Instrucciones para la ejecución
1. Clonar el repositorio
2. Editar el archivo config.txt con los parametros deseados        
3. Editar el archivo board.txt para usar el mapa deseado
4. Posicionarse en la carpeta y ejecutar el siguiente comando:
```
python3 ./main.py
```