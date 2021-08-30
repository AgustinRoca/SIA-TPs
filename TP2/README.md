## TP2: Algoritmos Geneticos

### Configuracion
La aplicacion recibe un unico parametro por linea de comandos, que es la ubicacion de un archivo json con las configuraciones de la aplicacion:
```json
{
    "outputPath": "(String) Archivo de salida. La carpeta debe existir.",
    
    "fillMethod": "(\"FILL_ALL\" | \"FILL_PARENTS\")",
    
    "player": {
        "type": "(\"WARRIOR\", \"ARCHER\", \"UNDERCOVER\", \"DEFENDER\")",
        "count": "(Integer) N > 0 que representa tamaño de poblacion",
        "selection": "(Integer) K > 0 que representa cantidad a seleccionar",
        "height": {
            "random": true
        } | {
            "random": false,
            "interval": {
                "min": "(Double) en [0.01, 0.09]",
                "max": "(Double) en [0.1, 0.19]"
            },
            "direction": "(Double) en [0, 1]. Probabilidad de disminuir o aumentar la altura (si <0.5, hay mas probabilidad de disminuir)"
        }
    },
    
    "equipment": {
        "inMemory": "(Boolean) Si esta seteado almacena la informacion en memoria"
        "boots": "(String) Path to tsv",
        "gloves": "(String) Path to tsv",
        "helmet": "(String) Path to tsv",
        "vest": "(String) Path to tsv",
        "weapon": "(String) Path to tsv"
    },
    
    "mutation": {
        "type": "(\"COMPLETE\", \"GEN\"",
        "probability": "(Double) en [0, 1]. Probabilidad de mutacion"
    } | {
        "type": "(\"MULTIGEN_LIMITED\", \"MULTIGEN_UNIFORM\")",
        "probability": "(Double) en [0, 1]. Probabilidad de mutacion",
        "multigenLimitedM": "(Integer) M > 0. Representa el indice hasta el cual se puede mutar"
    },
    
    "crossover": {
        "type": "(\"SINGLE_POINT\" | \"TWO_POINTS\" | \"ANNULAR\")"
    } | {
        "type": "UNIFORM",
        "probability": "(Double) en [0, 1]. Probabilidad de cruzar dos genes",
        "threshold": "(Double) en [0, 1]. Cruce uniforme"
    },

    "stopCriteria": {
        "criteria": "GENERATIONS",
        "parameter": "(Integer) N > 0 Cantidad de generaciones"
    } | {
        "criteria": "TIMEOUT",
        "parameter": "(Long) T > 0 Tiempo en milisegundos"
    } | {
        "criteria": "ACCEPTABLE_SOLUTION",
        "parameter": "(Double) F > 0 Fitness aceptado"
    } | {
        "criteria": "CONTENT",
        "parameter": "(Integer) N > 0 Cantidad de generaciones por la que un fitness se mantiene"
    } | {
        "criteria": "STRUCTURE",
        "parameter": "(Integer) N > 0 Cantidad de generaciones por la cual un porcentaje de la poblacion no presenta cambios",
        "percentage": "(Double) Porcentaje de la poblacion que no presenta cambios"
    },

    "selection": {
        "methodA": "(\"ELITE\" | \"ROULETTE\" | \"UNIVERSAL\" | \"BOLTZMANN\" | \"TOURNAMENT_DETERMINISTIC\" | \"TOURNAMENT_PROBABILISTIC\" | \"RANKING\")",
        "methodB": "(\"ELITE\" | \"ROULETTE\" | \"UNIVERSAL\" | \"BOLTZMANN\" | \"TOURNAMENT_DETERMINISTIC\" | \"TOURNAMENT_PROBABILISTIC\" | \"RANKING\")",
        "factor": "(Double) en [0, 1]. Representa fraccion de usar para metodo A y B"
    },

    "replacement": {
        "methodA": "(\"ELITE\" | \"ROULETTE\" | \"UNIVERSAL\" | \"BOLTZMANN\" | \"TOURNAMENT_DETERMINISTIC\" | \"TOURNAMENT_PROBABILISTIC\" | \"RANKING\")",
        "methodB": "(\"ELITE\" | \"ROULETTE\" | \"UNIVERSAL\" | \"BOLTZMANN\" | \"TOURNAMENT_DETERMINISTIC\" | \"TOURNAMENT_PROBABILISTIC\" | \"RANKING\")",
        "factor": "(Double) en [0, 1]. Representa fraccion de usar para metodo A y B"
    },
    
    "tournamentProbabilistic": {
        "probability": "(Double) en [0, 1] Probabilidad de seleccion para metodo Torneo Probabilistico",
        "window": "(Integer) W > 0 natural que representa la ventana para metodo Torneo Probabilistico"
    },
    
    "boltzmann": {
        "t0": "(Double) Temperatura inicial para metodo de Boltzmann",
        "tk": "(Double) Temperatura base para metodo de Boltzmann",
    },
}
```

**Nota**: La configuracion de "tournamentProbabilistic" y "boltzmann" son necesarios solamente si los mismos fueron utilizados como
metodos de seleccion o replacement.

Archivo de ejemplo en: config.example.json 

## Ejecucion

Correr la siguiente linea en una terminal:

```bash
java -jar TP2.jar <path config>
```
