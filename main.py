import pandas as pd
from comercio_scraper import Scraper
from options import UserOptions
from helpers import Helper
import os
import json


class ElComercio:
    """ Un scraper de las paginas del diario peruano El Comercio.
        Se extrae el titulo, breve descripción y el enlace de referencia """
    def __init__(self, main_url, news_number):
        self.main_url = main_url
        self.news_number = news_number

    #Funcion que exporta datos en diferentes formatos, format_option: 1: CSV ,  2: JSON
    def export(self, output):
        if output == 1:
            self._export_to_csv()
        elif output == 2:
            self._export_to_json()

    # Haciendo el data-frame y exportandolo a un archivo .csv:
    def _export_to_csv(self):
        news = Scraper(self.main_url, self.news_number)
        news_scraper = pd.DataFrame({
            'TITULAR': news.header_scraper(),
            'DESCRIPCIÓN': news.description_scraper(),
            'LINKS': news.link_scraper()
        })
        news_scraper.to_csv(f"./csv_files/{Helper.filename_generator(1)}")

    # Haciendo el json y exportandolo a un archivo .json:
    def _export_to_json(self):
        news = Scraper(self.main_url, self.news_number)
        keys = ['title', 'description', 'link']
        news_array = [ { keys[n]: value for n,value in enumerate(new) } for new in zip(news.header_scraper(), news.description_scraper(), news.link_scraper())]
        json_object = json.dumps(news_array, indent = 4) 
        filename = f"./json_files/{Helper.filename_generator(2)}"
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, 'x') as output_file:
            output_file.write(json_object)
            


if __name__ == "__main__":

    name = UserOptions(input('¿Cual es tu nombre: '))
    name.greeting()
    try:
        p_number = int(input('¿Cuantas noticias deseas investigar? (max. 50): '))
        if p_number > 50 or p_number < 0:
            raise ValueError('Por favor inserte un número de página valido (valor entero)')
        output = int(input('¿En que formato quieres recibir las noticias?\n1. CSV\n2. JSON\n\nEleccion: '))
        if output < 1 or output > 2:
            raise ValueError('Por favor inserte un número de opción valido (1 o 2)')

        elcomercio = ElComercio('https://elcomercio.pe/noticias/coronavirus/',
                                p_number)

        elcomercio.export(output)

        name.progress_bar()

        print(f'¡LISTO!, puedes revisar el archivo: "{Helper.filename_generator(output)}" dentro de la carpeta: "{Helper.folder_generator(output)}"')

    except ValueError as ex:
        print(ex)
