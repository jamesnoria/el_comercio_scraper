from progress.bar import Bar
import time


class UserOptions:
    """
    Clase para agregar decoración visual y
    opciones al usario al arrancar el programa.

    Attributes:
        name (str): Nombre de usario.

    """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Saludo inicial """
        print(' *'*29)
        print(f'Bienvenid@ {self.name.title()} a las noticias sobre el COVID-19'.center(60))
        print(' *'*29)
        print('Haré un archivo .csv para ti con la información más importante')

    def filename_generator(self):
        """ Generador de archivo .csv segun fecha
        cuando se realiza la solicitud al servidor """
        filename = time.strftime('%d_%m_%Y')
        file_format = 'covid_' + filename + '.csv'
        return file_format

    def progress_bar(self):
        """ Barra de progreso para denotar avance
        en la carga del tiempo que le toma al programa
        hacer el scraper y generar el archivo .csv """
        with Bar('Generando información') as bar:
            for i in range(100):
                time.sleep(0.02)
                bar.next()
        print(f'¡LISTO!, puedes revisar el archivo: "{self.filename_generator()}" dentro de la carpeta: "csv_files"')
