from django.shortcuts import render, redirect
from .forms import apiFormatForm
from .apiRequest import ApiHandler, DataHandler
import json

# Methodo de landing page


def home(request):

    # En caso de que el request 'POST' captura las 2 fechas ingresadas
    # Se convierten en cadenas y son enviadas en la URL al momento de redirigir
    # a la URL de 'data' y el formato de las fechas esta configurada en "YYYY-mm-dd"
    if request.method == 'POST':
        filled_form = apiFormatForm(request.POST)
        if filled_form.is_valid():
            initial_date = filled_form.cleaned_data['Fecha_inicial']
            final_date = filled_form.cleaned_data['Fecha_final']
            dates = str(initial_date)+" "+str(final_date)
            return redirect('data', dates=dates)
    # en caso de que el request no sea 'POST' se extrae el formato FORM 'apiFormatForm' en una variable
    # que incluye 2 formatos para ingresar fechas y termina haciendo una peticion de ser renderizada
    form = apiFormatForm()
    return render(request, 'home.html', {'form': form})

# Methodo que recibe 2 fechas y llama a un objeto que procesa la informacion de la API de banxico


def data(request, dates):
    # Se recibe una variable str con las 2 fechas separadas por un espacio.
    # Se separan ambas en una lista y luego se extraen cada una en una variable
    dates = dates.split()
    initial_date = dates[0]
    final_date = dates[1]

    # Variables que mandan a llaman al methodo "my_banxico_api" del objecto ApiHandler
    # enviando como datos requeridos, la fecha inicial, fecha final y el ID de la serie de datos
    # y guardan la lo que sea que recivan de regreso
    # variables para los UDIs
    udi_data = ApiHandler.my_banxico_api(initial_date, final_date, "SP68257")
    # se extrae la informacion anidada del json para facilidad de uso
    udis_dict = udi_data["bmx"]["series"][0]["datos"]
    # variables para los dolares
    dlr_data = ApiHandler.my_banxico_api(initial_date, final_date, "SF63528")
    dlr_dict = dlr_data["bmx"]["series"][0]["datos"]

    # Variables que mandan a llamar methodos para procesar los datos dentro del objeto de DataHandler
    # Y guardan lo que sea que recivan de regreso
    # Variables para procesar los UDIs
    # Variable para el valor maximo de los datos
    max_val_udis = DataHandler.max_val_handler(udis_dict)
    # Variable para el valor minimo de los datos
    min_val_udis = DataHandler.min_val_handler(udis_dict)
    # Debido a una diferencia de interpretacion entre Python y JS, se reaplica un interprete de json y se guarda en una nueva variable
    udis_json = json.dumps(udi_data)
    # Variables para procesar los dolares
    max_val_dlrs = DataHandler.max_val_handler(dlr_dict)
    min_val_dlrs = DataHandler.min_val_handler(dlr_dict)
    dlr_json = json.dumps(dlr_data)

    # Peticion de renderizado con todas las variables a ser interpretadas en el template
    return render(request, 'data.html', {
        'max_val_udis': max_val_udis,
        'min_val_udis': min_val_udis,
        'udis_json': udis_json,
        'max_val_dlrs': max_val_dlrs,
        'min_val_dlrs': min_val_dlrs,
        'dlr_json': dlr_json,
    })
