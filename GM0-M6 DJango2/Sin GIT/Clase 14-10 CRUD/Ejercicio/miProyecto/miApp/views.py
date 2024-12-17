from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from datetime import datetime
from django.contrib import messages
from .forms import PostForm


def listar_posts(request):
    posts = Post.objects.all()
    return render(request, "miApp/listar_posts.html", {"posts": posts})


def crear_post(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        contenido = request.POST["contenido"]
        messages.success(request, "¡El post ha sido creado con éxito!")
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


def post_comment(request, new_comment):
    if request.session.get("has_commented", False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session["has_commented"] = True
    return HttpResponse("Thanks for your comment!")
