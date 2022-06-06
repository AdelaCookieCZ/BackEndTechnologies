from django import forms
from django.core.exceptions import ValidationError

from .models import Animal


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class AnimalForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Animal
        fields = '__all__'