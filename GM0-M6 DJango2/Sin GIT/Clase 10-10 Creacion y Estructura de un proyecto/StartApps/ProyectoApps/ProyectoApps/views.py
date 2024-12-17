from django.shortcuts import render


# Funcion pagina de inicio
def index(request):
    return render(request, "index.html")
