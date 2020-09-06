# Scraper del diario peruano "El Comercio"

![image](https://drive.google.com/uc?export=view&id=1i-gHILYoR5i6iXEqkq1Fzdjtc8s3pldG)

## Descripción:

- Este proyecto personal realiza el proceso conocido como 'web scraping' a la página web del diario peruano **'El Comercio'** con un enfoque únicamente en el tema (topic) del coronavirus. El resultado final es un archivo `.csv` con tres columnas y su debida información respectivamente: Título, Descripción y link o enlace de referencia.

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

- Por cada página existe un aproximado de 50 noticias.

- La velocidad de respuesta es condicianado por una conexión estable a internet y/o la respuesta del servidor(es) del diario.

## To-Do:
(*siéntase libre de colaborar*)

- Condicionar el script a la respuesta del servidor (requests).
- Incluir otros temas o enfoques del diario.
- Hacer 'refactoring' un poco más.

## Licencia:

- Ver `LICENSE` para mayor información.

## Contacto:

- [![Twitter Badge](https://img.shields.io/badge/-James_Noria-1ca0f1?style=flat-square&logo=twitter&logoColor=white&link=https://twitter.com/jamesnoria)](https://twitter.com/jamesnoria) [![Gmail Badge](https://img.shields.io/badge/-jamesnoria@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:jamesnoria@gmail.com)](mailto:jamesnoria@gmail.com) [![Chat on Telegram](https://img.shields.io/badge/Chat%20on-Telegram-brightgreen.svg)](https://t.me/jamesnoria)