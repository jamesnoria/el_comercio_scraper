
import requests
from bs4 import BeautifulSoup

class Scraper:
    """ Clase para extraer la información necesaria, en este caso del diario: El Comercio """

    def __init__(self, url):
        self.url = url

    def main_scraper(self):
        page = requests.get(self.url)
        datos = BeautifulSoup(page.content, 'lxml')
        research = datos.find_all('div', class_ = 'story-item__information-box w-full') 
        return research

    def header_scraper(self):
        titulares = []
        for dato in self.main_scraper():
            titulares.append(dato.h2.a.text)
        return titulares

    def description_scraper(self):
        descripcion = []
        for dato in self.main_scraper():
            descripcion.append(dato.p.text)
        return descripcion

    def link_scraper(self):
        links = []
        for dato in self.main_scraper():
            links.append('https://elcomercio.pe' + dato.h2.a['href'])
        return links