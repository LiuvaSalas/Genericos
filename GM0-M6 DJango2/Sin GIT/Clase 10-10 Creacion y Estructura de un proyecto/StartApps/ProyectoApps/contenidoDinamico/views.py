from django.shortcuts import render


def contenidoDinamico(request):
    categories = ["Python", "Django", "HTML", "CSS", "JavaScript"]
    context = {"categories": categories}
    return render(request, "contenidoDinamico.html", context)
