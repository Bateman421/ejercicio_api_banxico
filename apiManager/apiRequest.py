from types import NoneType
import requests
import simplejson as json

# Objeto para procesar el API de banxico


class ApiHandler():
    # Methodo que recive 3 variables no opcionales y del tipo cadena para armar el URL y hacer una peticion a la API de banxico
    # @initial_date - Fecha de donde empezara la peticion
    # @final_date - Fecha donde termina la peticion
    # @id_series - Id de la serie de datos para la peticion
    def my_banxico_api(initial_date, final_date, id_series):
        endpoint = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/"
        token = "33cd47e7bd0856a96c0af10bd80ea3fc988303641253f566629ee4d567492224"
        response = requests.get(endpoint+id_series+"/datos/" +
                                initial_date+"/"+final_date+"?token="+token)

        data = response.json()
        return data

# Objeto con 2 methodos para procesar la informacion que reciben


class DataHandler:
    # Metodo que recibe un dictionario de datos pre-arreglado y busca el valor mas alto en el diccionario
    # @dict - Diccionario de datos en el cual dentro deben ir valores en Float en la columna 'dato'
    def max_val_handler(dict):
        max_val = 0.0
        for i in dict:
            current = float(i['dato'])
            if max_val < current:
                max_val = current
        return max_val

    # Metodo que recibe un dictionario de datos pre-arreglado y busca el valor mas bajo en el diccionario
    # @dict - Diccionario de datos en el cual dentro deben ir valores en Float en la columna 'dato'
    def min_val_handler(dict):
        min_val = float(dict[0]['dato'])
        for i in dict:
            current = float(i['dato'])
            if min_val > current:
                min_val = current
        return min_val
