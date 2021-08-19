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
    2. algorithm=1/2/3/4/5/6: decide el algoritmo a utilizar, siendo:
        1. BFS
        2. DFS
        3. IDDFS
        4. GGS
        5. A*
        6. IDA*
    3. heuristic=1/2/3: decide la heurística a utilizar en caso de que se use un algoritmo informado, siendo:
        1. Menor suma de las distancias de cada caja a un objetivo distinto no ocupado
        2. Suma de las distancias de cada caja a su objetivo más cercano no ocupado
        3. Suma de las distancias de cada caja a su objetivo más cercano no ocupado y la distancia del jugador a la caja más cercana
    4. limit=XX: límite inicial para el IDDFS
    5. file=filename: nombre del archivo que contiene el tablero

Ejemplo de config.txt:

    consider_deadlock=True
    algorithm=1
    heuristic=1
    limit=50
    file=TP1/boards/board.txt

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

## Juegos ejemplo:
- [board.txt](http://www.game-sokoban.com/index.php?mode=level&lid=200)
- [board2.txt](http://www.game-sokoban.com/index.php?mode=level&lid=45427)
- [board3.txt](http://www.game-sokoban.com/index.php?mode=level&lid=45426)

## Instrucciones para la ejecución
1. Clonar el repositorio
2. Editar el archivo config.txt con los parametros deseados        
3. Editar el archivo board.txt para usar el mapa deseado
4. Posicionarse en la carpeta y ejecutar el siguiente comando:
```
python3 ./main.py
```