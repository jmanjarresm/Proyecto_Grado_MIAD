# Herramienta de visualización para el monitoreo y análisis de clientes no regulados en la empresa Electro Dunas S.A.A

![Grupo de Energía de Bogota](./IMGS/logoGEB.png)


<div align="center">
  ¿Cómo podemos monitorear y determinar los consumos anomalos de los clientes no regulados dando uso a sus datos históricos de consumo para ayudar al Grupo Energético de Bogotá con su toma de decisiones?  
  <br />
  <a href="#acerca-de"><strong>Explorar gráficas »</strong></a>
  <br />
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/jmanjarresm/Proyecto_Final_Aprend_Sup_g17.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/dfgomezc/aribnb_optimize_prices/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![Propuesta Inicial](https://img.shields.io/badge/Propuesta-Inicial-green)](https://github.com/jmanjarresm)

</div>

<details open="open">
<summary>Tabla de Contenido</summary>

- [Acerca de](#acerca-de)
  - [Creado con](#creado-con)
- [Empezando](#empezando)
  - [Prerrequisitos](#prerrequisitos)
- [Usos](#usos)
- [Hoja de Ruta](#hoja-de-ruta)
- [Soporte](#soporte)
- [Contribuciones](#contribuciones)
- [Autores](#autores)
- [Licencia](#licencia)
- [Agradecimientos](#agradecimientos)

</details>

---

## Acerca de

<table><tr><td>


Electro Dunas S.A.A es una empresa de distribución y comercialización de energía eléctrica en Perú que pertenece al grupo de Energía de Bogotá en Colombia. La empresa está orientada a la prestación del servicio público de distribución de energía eléctrica y alumbrado público, tanto a clientes residenciales como empresas y entidades gubernamentales. La calidad en los procesos operativos que intervienen en las actividades anteriores influye directamente en el objetivo estratégico de la empresa de cumplir de las expectativas de clientes e inversionistas. Lo anterior acompañado de la visión de ser líderes en el mercado se buscan poner en marcha estrategias de innovación y gestión de riesgos para la compañía que brinden herramientas para la gestión y toma de decisiones.  

Entre sus clientes están los clientes no regulados o libres, con un nivel de consumo anual de más de 2,5 MW en cada punto de suministro. Para el año 2022 este segmento de clientes fue el de mayor actividad por lo que la compañía y sus inversionistas están interesados en conocer el comportamiento de consumo e identificar posibles anomalías. Este repositorio se enfoca en la exploración de modelos analíticos que permitan identificar anomalías, bajo la condición de no contar con información histórica de estas, lo que conlleva a la necesidad de emplear modelos no supervisados que puedan detectar patrones anómalos. 

Con base en lo anterior, se han seleccionado tres algoritmos ampliamente utilizados en la detección de anomalías en el consumo energético: Isolation Forest, K-Means y OCSVM (One Class Support Vector Machine). Estos modelos ofrecen la flexibilidad y la eficacia necesarias para abordar la complejidad de los datos energéticos y adaptarse a las necesidades específicas de la entidad. 

A lo largo de este respositorio, se detallará el proceso metodológico utilizado, desde la preparación de datos hasta la evaluación de modelos, destacando la integración coherente de modelos descriptivos y la detección de anomalías. Además, se analizarán los resultados obtenidos, se identificarán posibles ajustes y se establecerá un plan para la implementación del prototipo funcional que se creara con aquel modelo que presente los mejores resultados.


La estructura de carpetas para almacenar la información es:

- **INPUTS**: En esta carpeta se almaceno toda la información de entrada al modelo de machine learning. Por temas de confidencialidad esta información no se encuentra en el repositorio pero en los notebook se pueden observar los resultados del uso de la misma para la evaluación de modelos.
 - **OUTPUTS**: En esta carpeta van a estar todas las salidas que se necesiten para el despliegue del modelo. Al interior de esta carpeta se van a encontrar las anomalías detectadas y otras salidas
- **IMGS**: Carpeta de imágenes para los .README, notebooks.
- **SCRIPTS**: Los scripts van a estar numerados y nombrados de acuerdo a la evolución del proyecto.
- **DOCS**: En esta carpeta se van a almacenar todos los documentos de referencia, metadatos, plan de datos, resultados y todos los documentos que no se puedan clasificar en las carpetas anteriores.
- **ENTRADA**: En la primera página del repositorio se podran encontrar los notebooks que fueron utilizados para la evaluación de la calidad de la información y la evaluación de cada modelo.

</td></tr></table>

### Creado con

En este repositorio, se ha realizado un análisis de datos y modelos No Superivsados Isolation Forest, K-Means y OCSVM utilizando Python como herramienta principal.

#### Uso de Python

Para el desarrollo del proyecto se da uso a Python para todo el proceso de análisis de datos. Python nos proporciona una amplia gama de bibliotecas y herramientas para realizar análisis de datos de manera efectiva, lo que incluye la limpieza de datos, la visualización de resultados y la implementación de algoritmos de análisis de anomalías.

#### Isolation Forest

El algoritmo Isolation Forest fue seleccionado para ser evaluado debido a su uso en varias oportunidades para la detección de anomalías en el consumo de energía y su bajo costo computacional.

#### K-Means

El algoritmo K-Means due seleccionado para su evaluación por su simplicidad y eficacia en identificar clústeres de datos, lo que ayuda a identificar patrones normales de comportamiento del consumo de energía. Además de lo anterior está el hecho de que se ha aplicado en múltiples ocasiones en la industria para la detección de datos anómalos.

#### One-Class Support Vector Machine (OCSVM) 

El algoritmo OCSVM fue elegido por su capacidad para encontrar la región de datos más densa y distinguir entre puntos normales y anómalos en un espacio multidimensional. Esto lo hace particularmente adecuado para detectar anomalías en conjuntos de datos energéticos, donde es crucial identificar desviaciones significativas del comportamiento esperado.

## Empezando

### Prerrequisitos

Para trabajar en este proyecto y ejecutar los análisis de datos y puntos calientes, se deben cumplir con los siguientes prerrequisitos:

Python: Tener Python instalado en el sistema. Este proyecto se ha desarrollado utilizando Python 3. Se puede descargar Python desde python.org.

Bibliotecas de Python: Instalar las bibliotecas de Python necesarias utilizando el gestor de paquetes pip. Se debe instalar ejecutando el siguiente comando en la terminal:

pip install pandas matplotlib seaborn scikit-learn

Estas bibliotecas son esenciales para el análisis de datos, visualización y análisis de anomalías en Python.

## Usos

Este repositorio muestra el proceso de evaluación que se realizó a los diferentes modelos para identificar aquel que mejor detecta anomalías se podra observar el paso a paso en esta determinación acompañado por el documento [Proyecto](https://github.com/dfgomezc/aribnb_optimize_prices/blob/main/DOCS/Mejorando_la_Competitividad_en_Airbnb-_Optimizaci%C3%B3n_de_Precios_de_Alquiler_en_Nueva_York_V4.pdf)
En el que se podrá ver los resultados encontrados.

## Autores

El Repositorio fue creado por [Juan Felipe Manjarres](https://github.com/jmanjarresm).

El Proyecto fue realizado por:
- Mayra Neisa
- Lina Marcela Ladino

Para ver todos los autores ver la [página de contribuciones](https://github.com/jmanjarresm/Proyecto_Grado_MIAD/graphs/contributors).


## Licencia

Este proyecto esta licenciado bajo **MIT license**.

Ver [LICENCIA](LICENSE) para más información.

## Agradecimientos

Se agradece el apoyo de la Universidad de los Andes en el desarrollo de este proyecto


