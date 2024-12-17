from django.shortcuts import render


# Funcion pagina de inicio
def blogs(request):
    return render(request, "blogs.html")
