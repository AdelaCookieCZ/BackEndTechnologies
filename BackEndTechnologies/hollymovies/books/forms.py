from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from books.models import BaseBook, Author


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class DateFieldSevenDaysFromNow(forms.DateField):
    widget = DatePickerDateInput

    def validate(self, value):
        super(DateFieldSevenDaysFromNow, self).validate(value)
        if value < timezone.now().date() + timedelta(days=7):
            raise ValidationError('Cannot create contact at earlier that 7 days from now')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()      #dedi z charfieldu
    subject = forms.CharField(widget=forms.Textarea())
    phone_number = forms.IntegerField()
    age = forms.IntegerField(min_value=1, max_value=99)
    contact_at = DateFieldSevenDaysFromNow()


class BookForm(forms.ModelForm):
    released = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = BaseBook
        fields = '__all__'
        exclude = ['likes', ]


class AuthorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Author
        fields = '__all__'
