from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.listar_posts, name="listar_posts"),
    path("posts/create/", views.crear_post, name="crear_post"),
    path("posts/update/<int:id>/", views.actualizar_post, name="actualizar_post"),
    path("posts/delete/<int:id>/", views.eliminar_post, name="eliminar_post"),
]
