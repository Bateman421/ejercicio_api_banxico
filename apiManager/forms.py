from django import forms
from django.forms import ModelForm
from django.forms import widgets
from .models import Dates
from bootstrap_datepicker_plus import DatePickerInput


class DatesInput(forms.DateInput):
    input_type = 'date'


class apiFormatForm(ModelForm):
    # formato Form basado en el modelo Dates para generar 2 cambos de fechas usando el widget "DatePickerInput"
    # de la libreria de bootstrap, por default usa un formato "YYYY-mm-dd"
    class Meta:
        model = Dates
        fields = ['Fecha_inicial', 'Fecha_final']
        widgets = {
            'Fecha_inicial': DatePickerInput(
                options={
                    "format": "YYYY-MM-DD",
                }
            ),
            'Fecha_final': DatePickerInput(
                options={
                    "format": "YYYY-MM-DD",
                }
            ),

        }
