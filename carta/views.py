from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
# request -> response
# hacer llamdos a la base de datos
# enviarles emails a los clientes
def home(request):
    return render(request, "home.html")

def carta(request):

    productos = Product.objects.all()
    return render(request, "carta.html", {"productos": productos})

def ubicacaciones(request):
    return render(request, "ubicaciones.html")