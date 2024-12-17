from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from datetime import datetime


def listar_posts(request):
    posts = Post.objects.all()
    return render(request, "miApp/listar_posts.html", {"posts": posts})


def crear_post(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        contenido = request.POST["contenido"]
        nuevo_post = Post(
            titulo=titulo, contenido=contenido, fecha_publicacion=datetime.now()
        )
        nuevo_post.save()
        return redirect("listar_posts")
    return render(request, "miApp/crear_post.html")


def actualizar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.titulo = request.POST["titulo"]
        post.contenido = request.POST["contenido"]
        post.save()
        return redirect("listar_posts")
    return render(request, "miApp/actualizar_post.html", {"post": post})


def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("listar_posts")
