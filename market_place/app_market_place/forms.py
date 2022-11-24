from django import forms


class AddGoodToCart(forms.Form):
    quantity = forms.IntegerField(help_text='Количество', required=True)
