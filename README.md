### Análisis Exploratorio de Datos: Evolución del Precio del Alquiler en España

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre la evolución del precio del alquiler en España durante los últimos diez años. Se utiliza un conjunto de datos público que contiene información mensual sobre los precios del alquiler en varias ciudades y regiones de España.
Datos

Los datos utilizados en este análisis provienen de INE, INJUVE, insideairbnb, CIS. El conjunto de datos incluye:

    Fecha: Mes y año del registro del precio del alquiler.
    Ubicación: Ciudad o región específica en España.
    Precio: Precio medio del alquiler en euros.

Objetivos

El objetivo principal de este análisis es explorar cómo han fluctuado los precios del alquiler en diferentes partes de España a lo largo del tiempo. Se pretende identificar tendencias, patrones estacionales y cualquier cambio significativo en los precios.
Contenido del Repositorio

    data/: Carpeta que contiene los datos originales en formato CSV.
    utils/: Carpeta que contiene un archivo python con funciones para la lectura y procesamiento de los documentos en formato CSV.
    src/: Carpeta que contiene el notebook Jupyter utilizado para el análisis, y los datos procesados en formato CSV.
    README.md: Este archivo que proporciona una descripción del proyecto.

Análisis Realizado

El análisis exploratorio incluye los siguientes pasos:

    Carga y Limpieza de Datos: Procesamiento inicial de los datos para eliminar datos faltantes o inconsistentes.

    Análisis Descriptivo: Visualización de la distribución de los precios del alquiler y estadísticas descriptivas.

    Análisis Temporal: Exploración de cómo han variado los precios a lo largo del tiempo, identificación de patrones estacionales o tendencias a largo plazo.

    Análisis Geográfico: Comparación de precios entre diferentes ciudades y regiones de España.

    Conclusiones: Resumen de los hallazgos clave y posibles insights sobre la evolución del mercado de alquiler en España.

Ejecución del Código

Para ejecutar el análisis por ti mismo, sigue estos pasos:

    Clona este repositorio en tu máquina local:

    bash

    git clone https://github.com/aliciamb86/EDA.git

    Abre el notebook Jupyter src/memoria.ipynb y ejecuta las celdas en un entorno de Python con las bibliotecas necesarias instaladas.

Dependencias

El análisis se ha realizado utilizando Python 3 y las siguientes bibliotecas principales:

    Pandas
    Matplotlib
    Seaborn

Para instalar las dependencias, puedes utilizar pip:

pip install pandas matplotlib seaborn

Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor abre un issue para discutir los cambios propuestos o envía un pull request.
Autor

    Nombre: Alicia Martínez
    GitHub: aliciamb86

