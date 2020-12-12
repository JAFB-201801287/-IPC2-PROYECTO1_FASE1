from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cuentas(request):
    return render(request, 'cuentas.html')

def detalle_cuenta(request):
    return render(request, 'detalleCuenta.html')

def retiro(request):
    return render(request, 'retiro.html')
