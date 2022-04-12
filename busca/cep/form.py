from django import forms

class CepForm(forms.Form):
    cep = forms.CharField(max_length=8, widget=forms.NumberInput(attrs={"class":"cep", "placeholder":"Digite um cep de 8 dígitos"}))