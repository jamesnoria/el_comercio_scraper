import pandas as pd
import time
from comercio_scraper import Scraper
from options import UserOptions


class ElComercio:
    """ Un scraper de las paginas del diario peruano El Comercio.
        Se extrae el titulo, breve descripción y el enlace de referencia """

    def __init__(self, main_url, news_number):
        self.main_url = main_url
        self.news_number = news_number

    # Generando un archivo .csv con la fecha de referencia:
    def filename_generator(self):
        filename = time.strftime('%d_%m_%Y')
        return 'covid_' + filename + '.csv'

    # Haciendo el data-frame y exportandolo a un archivo .csv:
    def export_to_csv(self):
        news = Scraper(self.main_url, self.news_number)
        news_scraper = pd.DataFrame({
            'TITULAR': news.header_scraper(),
            'DESCRIPCIÓN': news.description_scraper(),
            'LINKS': news.link_scraper()
        })
        news_scraper.to_csv(f'./csv_files/{self.filename_generator()}')


if __name__ == "__main__":

    name = UserOptions(input('¿Cual es tu nombre: '))
    name.greeting()
    try:
        p_number = int(input('¿Cuantas noticias deseas investigar? (max. 50): '))
        elcomercio = ElComercio('https://elcomercio.pe/noticias/coronavirus/',
                                p_number)
        elcomercio.export_to_csv()
        name.progress_bar()
    except ValueError:
        print('Porfavor inserte un número de página valido (valor entero)')
