
from progress.bar import Bar
import time

class UserOptions:
    """ Clase para agregar decoración visual al usario """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(' *'*29)
        print(f'Bienvenid@ {self.name.title()} a las noticias sobre el COVID-19'.center(60))
        print(' *'*29)
        print('Haré un archivo .csv para ti con la información más importante')

    def filename_generator(self):
        filename = time.strftime('%d_%m_%Y')
        file_format = 'covid_' + filename + '.csv'
        return file_format

    def progress_bar(self):
        with Bar('Generando información') as bar:
            for i in range(100):
                time.sleep(0.02)
                bar.next()
        print(f'¡LISTO!, puedes revisar el archivo: "{self.filename_generator()}" dentro de la carpeta: "csv_files"')