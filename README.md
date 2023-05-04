[![Contributors][contributors-shield]][contributors-url]
![Stargazers][stars-shield]
[![License][license-shield]][license-url]


<br />
<p align="center">
  <h3 align="center">Sistema de Autenticación por Reconocimiento Facial</h3>
  <p align="center">
    Facial Recognition
  </p>
</p>




Este proyecto presenta un sistema de autenticación mediante el reconocimiento facial, utilizando Django para el procesamiento de imágenes y técnicas de aprendizaje automático. Este sistema consta de cuatro etapas, que se describen a continuación:

Adquisición de imágenes: se adquieren imágenes de rostros de estudiantes del Tecnológico de Monterrey Campus Toluca.
Extracción y vectorización de características: se extraen y vectorizan las características del rostro.
Reducción de dimensionalidad: se utilizan diferentes modelos (PCA, SVD e ISOmap) para reducir la dimensionalidad y extraer características importantes para la clasificación de los rostros.
Identificación del rostro: se asigna una ponderación a los resultados obtenidos en cada uno de los modelos para identificar el rostro en cuestión.
Este último paso se realiza como propuesta de solución para sistemas de reconocimiento facial ante un conjunto de datos limitado. Los resultados sugieren que el uso de técnicas de reducción de dimensiones y métricas de similitud adecuadas puede mejorar significativamente el rendimiento de los sistemas de reconocimiento facial.

Requisitos
Para poder utilizar este sistema de autenticación por reconocimiento facial, se necesitan los siguientes requisitos:

<ul>Python 3.10 o superior</ul>
<ul>Django 3.2 o superior</ul>
<ul>OpenCV 4.5 o superior</ul>
<ul>NumPy 1.20 o superior</ul>
<ul>Scikit-learn 0.24 o superior</ul>


Instalación
Para instalar este sistema de autenticación por reconocimiento facial, siga los siguientes pasos:

Clone este repositorio en su máquina local.

Instale los requisitos especificados en el archivo Pipfile utilizando PIPENV corriendo:

```
  pipenv install
```

Y una vez instalado corriendo:

```
  pipenv shell
```

Ejecute el archivo manage.py en la línea de comandos con el siguiente comando.

```
  python manage.py runserver
```



<ul>
  
  Para utilizar este sistema de autenticación por reconocimiento facial, siga los siguientes pasos:

  <li>Ingrese a la página web que se generó en el paso anterior (localhost:8000 por defecto).</li>

  <li>Seleccione la opción de "tomar foto" y siga las instrucciones para acceder al sistema</li>

  <li>Si el sistema identifica su rostro correctamente, tendrá acceso a la página de inicio.</li>
  
</ul>


Conclusiones
Este proyecto presenta un sistema de autenticación por reconocimiento facial robusto que utiliza técnicas de aprendizaje automático para reducir la dimensionalidad de las características del rostro y mejorar la precisión de la identificación. Además, el uso de frameworks como Django permite una implementación más fácil y rápida de sistemas avanzados como este. Este sistema puede tener un gran potencial de aplicación en distintos sectores, especialmente en el de seguridad para el control de acceso y la gestión de identidad en el ámbito laboral.


[contributors-shield]: https://img.shields.io/badge/CONTRIBUTORS-5-GREEN?style=for-the-badge
[contributors-url]: https://github.com/ANVRRT/FacialDetection/graphs/contributors
[stars-shield]: https://img.shields.io/badge/STARS-0-yellow?style=for-the-badge
[license-shield]: https://img.shields.io/badge/LICENSE-%20-green?style=for-the-badge
[license-url]: https://github.com/ANVRRT/Sales-registry-system-CRUD/blob/main/license.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
