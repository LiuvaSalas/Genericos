from django.shortcuts import render


def foro(request):
    return render(request, "foro.html")
