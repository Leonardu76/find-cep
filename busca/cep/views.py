from django.shortcuts import render
import requests
from .form import CepForm



# Create your views here.

def get_cep(request):
    a = None
    cepsent = False
    err = False
    if request.method == 'POST':
        # cria um formulario NameForm com os campos que foram digitados
        form = CepForm(request.POST)
        # checa se é um formulário válido:
        
        if form.is_valid():
            # pega o número digitado
            cep = form.cleaned_data['cep']
            url_base =  f'https://viacep.com.br/ws/{cep}/json/'
            r = requests.get(url_base)
            a = r.json()
            if 'cep' in a:
             cepsent = True
            # ...
            else:
                err = True

    # se a validação der erro vai aqui
    else:
        form = CepForm()

          


    return render(request, 'cep/index.html', {'form': form, 'a': a, 'cepsent':cepsent, 'err':err })