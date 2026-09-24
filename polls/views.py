from django.shortcuts import render
from django.http import HttpResponse


# Create your views here. (Visualizações do website)

# Página Principal (Home / Index)
def index(request):
    return render(request, 'polls/HTML/index.html')

# Página relacionada a Praia do Forte
def praia_do_forte(request):
    return render(request, 'polls/HTML/praia_do_forte.html')

# Página relacionada a Imbassaí
def imbassai(request):
    return render(request, 'polls/HTML/imbassai.html')










