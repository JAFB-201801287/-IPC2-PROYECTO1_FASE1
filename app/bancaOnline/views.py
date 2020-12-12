from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

#def cuentas(request):
#    return render(request, 'cuentas.html')
