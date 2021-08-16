# Scraper del diario peruano "El Comercio"

<div align="center">

<img alt="GitHub stars" src="https://img.shields.io/github/stars/jamesnoria/el_comercio_scraper?style=social"> <img alt="GitHub forks" src="https://img.shields.io/github/forks/jamesnoria/el_comercio_scraper?style=social"> <img alt="GitHub followers" src="https://img.shields.io/github/followers/jamesnoria?style=social">

</div>

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/jamesnoria/el_comercio_scraper) ![GitHub top language](https://img.shields.io/github/languages/top/jamesnoria/el_comercio_scraper) ![GitHub](https://img.shields.io/github/license/jamesnoria/el_comercio_scraper) ![GitHub last commit](https://img.shields.io/github/last-commit/jamesnoria/el_comercio_scraper)

</div>


![image](https://drive.google.com/uc?export=view&id=1i-gHILYoR5i6iXEqkq1Fzdjtc8s3pldG)

## Descripción:

- Este proyecto personal realiza un scraper de la página web del diario peruano **'El Comercio'** con un enfoque únicamente en el tema (topic) del coronavirus. El resultado final es un archivo `.csv` o `.json` con la debida información Título, Descripción y link o enlace de referencia (respectivamente).

## Pre-requisitos:

- Python 3.6 +
- pip
- Unix-shell (no excluyente)

## Como usarlo:

1. Clonar este repositorio:

    ```shell
    git clone https://github.com/jamesnoria/el_comercio_scraper.git
    ```

2. Acceder a la carpeta:

    ```shell
    cd el_comercio_scraper/
    ```

3. Instalar las librerias y paquetes necesarios (dentro de un ambiente virtual):

    ```shell
    pip install -r requirements.txt
    ```

4. Ejecutar el script:

    ```shell
    python3 main.py
    ```

5. Ver nuestro archivo `.csv` (se generan dentro de la carpeta 'csv_files'):

    ```shell
    ls ./csv_files/
    ```

## Notas:
- Los `.csv` generados incluyen la fecha de cuando se realizó la solicitud.

- El máximo de noticias a obtener son 50.

- La velocidad de respuesta es condicianado por una conexión estable a internet y/o la respuesta del servidor(es) del diario.

## To-Do:
(*siéntase libre de colaborar*)

- See Issues.
- Raise a new issue for any suggestion.

## Licencia:

- Ver `LICENSE` para mayor información.

## Contacto:

- [![Twitter Badge](https://img.shields.io/badge/-James_Noria-1ca0f1?style=flat-square&logo=twitter&logoColor=white&link=https://twitter.com/jamesnoria)](https://twitter.com/jamesnoria) [![Gmail Badge](https://img.shields.io/badge/-jamesnoria@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:jamesnoria@gmail.com)](mailto:jamesnoria@gmail.com)