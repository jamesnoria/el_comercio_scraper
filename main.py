
import pandas as pd
import csv
import time
from comercio_scraper import Scraper
from options import UserOptions

class El_Comercio:
    """ Un scraper de las paginas del diario peruano El Comercio.
        Se extrae el titulo, breve descripción y el enlace de referencia """

    def __init__(self, main_url, pages):
        self.main_url = main_url
        self.pages = pages

    # Por cada pag. hay 50 noticias, el user decide cuantas quiere extraer:
    def number_pages(self):
        urls = []
        contador = 0
        while contador < self.pages:
            contador += 1
            enlaces = self.main_url + (str(contador))
            urls.append(enlaces)
        return urls

    def get_headers(self):
        titulares = []
        for url in self.number_pages():
            loop = Scraper(url)
            titulares.extend(loop.header_scraper())
        return titulares

    def get_descriptions(self):
        descripcion = []
        for url in self.number_pages():
            loop = Scraper(url)
            descripcion.extend(loop.description_scraper())
        return descripcion

    def get_links(self):
        links = []
        for url in self.number_pages():
            loop = Scraper(url)
            links.extend(loop.link_scraper())
        return links 

    # Generando un archivo .csv con la fecha de referencia vigente a la busqueda:
    def filename_generator(self):
        filename = time.strftime('%d_%m_%Y')
        return 'covid_' + filename + '.csv'

    # Haciendo el data-frame y exportandolo a un archivo .csv:
    def export_to_csv(self):
        news_scraper = pd.DataFrame({
            'TITULAR' : self.get_headers(),
            'DESCRIPCIÓN' : self.get_descriptions(),
            'LINKS' : self.get_links()
        })
        news_scraper.to_csv(f'./csv_files/{self.filename_generator()}')

if __name__ == "__main__":

    name = UserOptions(input('¿Cual es tu nombre: '))
    name.greeting()
    try:
        p_number = int(input('¿Cuantas páginas deseas investigar?: '))
        elcomercio = El_Comercio('https://elcomercio.pe/noticias/coronavirus/', p_number)
        elcomercio.export_to_csv()
        name.progress_bar()
    except ValueError:
        print('Porfavor inserte un número de página valido (valor entero)')