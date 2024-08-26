from django.shortcuts import render, HttpResponse

# Create your views here.
# request -> response

def home(request):
    return render(request, "home.html")

def carta(request):
    return render(request, "carta.html")

def ubicacaciones(request):
    return render(request, "ubicaciones.html")