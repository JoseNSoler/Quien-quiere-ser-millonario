<h1 align="center">
  <br>
  <a><img src="https://generacionxbox.com/wp-content/uploads/2020/12/quien-quiere-ser-millonario.jpg" alt="Markdownify" width="400"></a>
  <br>
  ¿Quién quiere ser millonario?
  <br>
</h1>

<h4 align="center">Challenge: Concurso de preguntas y respuestas</h4>
<br>
[![GitHub license](https://img.shields.io/github/license/sultan99/react-on-lambda.svg)](https://github.com/JoseNSoler/Quien-quiere-ser-millonario/blob/master/README.md)  [![GitHub license](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)]()

## Descripcion V1.0

`main.py` es un programa de concurso de preguntas y respuestas, la intencion fue diseñar una solucion que permita tener un banco de preguntas con diferentes opciones para una unica respuesta, cada pregunta esta categorizada por niveles (5 en total), por cada ronda se asigna un premio acumulable, el programa acaba cuando el jugador introduce una pregunta incorrecta


## Como jugar

El programa fue desarrollado en Python 3.7.7, y requiere de una version de python igual o posterior, adicional de los modulos `pymongo` y `dnspython`, los cuales pueden ser instalados facilmente mediante el gestor de paquetes `pip` [como instalar pip en Windows, Mac y Linux](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)


```bash
$ pip install pymongo
$ pip install dnspython
```
<br>
El programa se puede descargar en formato zip y descomprimir, o clonar por HTTPS "git clone https://github.com/JoseNSoler/Quien-quiere-ser-millonario.git"
(Para windows, abrir una nueva ventana de comandos (cmd) por dentro de la carpeta descargada)

```bash
# Clonar el repositorio
$ git clone https://github.com/JoseNSoler/Quien-quiere-ser-millonario.git

# Ir a la carpeta creada por git clone, o la carpeta descomprimida del ZIP
$ cd Quien-quiere-ser-millonario

# Ejecutar directamente por medio de python
$ python main.py
```
***
# Opciones
<br>
<p align="center"><img src="https://i.imgur.com/sh9f7I7.png" alt="Markdownify" width="600" ></p>

El programa inicia dejando al usuario escojer entre:
* Iniciar el juego, empezando por introducir un ` nombre`  de jugador
* Ver los resultados que jugadores previos obtuvieron (Al finalizar la partida, el puntaje actual y el ` nombre`  se guardan publicamente en una base de datos MongoDB)
(`mongodb+srv://public:test@database.j4esf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority` Python 3.6 o posterior)

<br>
<p align="center"><img src="https://i.imgur.com/PuRRwMq.png" alt="Markdownify" width="400" ></p>

Al iniciar juego, se muestra informacion basica de el nivel y puntaje actual, asi como la pregunta a responder y las posibles respuestas en orden aleatorio, la respuesta a introducir debe ser igual a una de las opciones `A`, `B`, `C` o `D`;  El juego termina al introducir una respuesta erronea o escribiendo `rendirse`, convervando en ambas el maximo puntaje alcanzado

---

# Contribuidores
> GitHub [@josensoler](https://github.com/JoseNSoler) &nbsp;&middot;&nbsp;
