# Practica 2: Despliegue de un servicio Cloud Native

Esta práctica consiste en la creación, entrega/despliegue de un servicio Cloud Native completo desde la adquisición del código fuente, acceso a datos hasta la ejecución de contenedores, compuesto por una API de tipo HTTP RESTful que permita entregar un servicio de predicción de temperatura y humedad. Esta API debe tener como mínimo las siguientes operaciones, separadas en dos versiones, 1 y 2:
## Versión 1 del código del servicio (irá para CI/CD en contenedor)
    - HTTP GET EndPoint 1 → /servicio/v1/prediccion/24horas/
    - HTTP GET EndPoint 2 → /servicio/v1/prediccion/48horas/
    - HTTP GET EndPoint 3 → /servicio/v1/prediccion/72horas/
## Versión 2 del código del servicio (irá para CI/CD en contenedor)
    - HTTP GET EndPoint 4 → /servicio/v2/prediccion/24horas/
    - HTTP GET EndPoint 5 → /servicio/v2/prediccion/48horas/
    - HTTP GET EndPoint 6 → /servicio/v2/prediccion/72horas/

La funcionalidad de cada uno de los ​ EndPoints​ anteriores es realizar una predicción de Humedad y Temperatura para 3 intervalos: 24, 48 y 72 horas. Esta funcionalidad se ha implementado como una herramienta (o función en Python) para predecir en función de varios parámetros de entrada y está disponible en el link del sitio web de la práctica para temperatura 1 como para humedad 2 para la versión 1, donde se usa ARIMA para predecir ambas para las 24 horas siguientes, por lo que tendrás que adaptar esa versión a la versión 2, por ejemplo usando otro algoritmo como los de redes neuronales, random forest, etc.

- [Versión 1](https://github.com/natalia2911/P2AirflowForecast/tree/version1)
- [Version 2](https://github.com/natalia2911/P2AirflowForecast/tree/version1)
