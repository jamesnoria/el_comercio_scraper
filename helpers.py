import time


class Helper:
    """ Generando un archivo .csv o .json con la fecha de referencia,
    format_option: 1: CSV ,  2: JSON """
    def filename_generator(format_option):
        filename = time.strftime('%d_%m_%Y')
        if format_option == 1:
            format = "csv"
        elif format_option == 2:
            format = "json"
        return 'covid_' + filename + '.' + format

    def folder_generator(format_option):
        if format_option == 1:
            format = "csv"
        elif format_option == 2:
            format = "json"
        return f'{format}_files'
