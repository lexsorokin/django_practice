from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from app_users.models import Profile
from market_place import settings


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(help_text='Имя', max_length=100, required=True)
    last_name = forms.CharField(help_text='Фамилия', max_length=100, required=True)
    email = forms.EmailField(help_text='Электронная почта', required=True)
    phone = forms.IntegerField(help_text='Номер телефона', required=True)
    address = forms.CharField(help_text='Адрес', required=True)
    photo = forms.ImageField(help_text='Фотография', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2']


class EditProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']


class DepositForm(forms.Form):
    deposit = forms.IntegerField(help_text='Сумма пополнения', required=True)


class PeriodForReport(forms.Form):
    start_date = forms.DateField(required=True, input_formats=settings.DATE_INPUT_FORMATS)
    end_date = forms.DateField(required=True, input_formats=settings.DATE_INPUT_FORMATS)

