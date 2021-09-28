# Perceptron Simple y Multicapa

## Requerimientos

Debe tener instalado python3 y ejecutar
`pip install -r requirements.txt`

## Ejecución
Para ejecutar el programa se debe correr la siguiente linea desde el root del proyecto

`python3 main.py`

## Configuracion
Para poder configurar la red neuronal y los problemas a ejecutar es necesario modificar el archivo config.json como de la siguiente manera:
```json
{
    "training": {
        "input": "input/ej3-entrenamiento.txt",
        "output": "input/ej3b-salida-deseada.txt",
        "ratio": 50,
        "cross_validation": false,
        "training_ration": 10
    },
    "constants": {
        "eta": 0.01,
        "beta": 0.5,

        "system_threshold": 1,
        "error_threshold": 0.0,
        "count_threshold": 100,
        "a": 0.05,
        "delta_error_decrease_iterations": 10,
        "b": 0.1,
        "delta_error_increase_iterations": 15,
   	    "delta_results" : 0.1
    },
    "system": {
	    "layout": [10,10,10],
        "function": "step",
     	"normalize_output": true,
    	"trust_min": 0.7,
        "w": {
            "random": 1.0,
            "reset_iter": 100,
            "error_enhance": false
        }
    }
}
```
