import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


class Scraper:
    """ Local package que permite obtener las etiquetas(html),
    titulares, descripciones y links de las noticias en el sitio """

    def __init__(self, url, news_number):
        self.url = url
        self.news_number = news_number

    def main_scraper(self):
        """
        Solicitud al servidor y obtención del html

        Return:
            Elementos html (etiquetas) de la clase que contiene la
            caja con la información necesaria.

        """
        try:
            page = requests.get(self.url)
            page.raise_for_status()
        except HTTPError as http_err:
            print(f'Un error ha ocurrido: {http_err}')
        except Exception as err:
            print(f'Un error ha ocurrido : {err}')
        else:
            datos = BeautifulSoup(page.text, 'lxml')
            research = datos.find_all('div',
                                      class_='story-item__information-box w-full')
            return research

    def header_scraper(self):
        """
        Extracción de los titulares.

        Return:
            Lista con titulares dependientes del
            número solicitado.

        """
        titulares = []
        try:
            for dato in self.main_scraper()[:self.news_number]:
                titulares.append(dato.h2.a.text)
            return titulares
        except TypeError:
            pass

    def description_scraper(self):
        """
        Extracción de breve descripcion de la noticia.

        Return:
            Lista con las diferentes descripciones de cada
            una de las noticias.

        """
        descripcion = []
        try:
            for dato in self.main_scraper()[:self.news_number]:
                descripcion.append(dato.p.text)
            return descripcion
        except TypeError:
            pass

    def link_scraper(self):
        """
        Extracción de links de cada noticia.

        Return:
            Lista con links o urls de referencia.
        """
        links = []
        try:
            for dato in self.main_scraper()[:self.news_number]:
                links.append('https://elcomercio.pe' + dato.h2.a['href'])
            return links
        except TypeError:
            pass
