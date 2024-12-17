from django.contrib import admin
from .models import Post, Perfil


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "fecha_publicacion",
        "contenido_preview",
    )
    search_fields = ("titulo", "contenido")
    list_filter = ("fecha_publicacion",)
    ordering = ("-fecha_publicacion",)
    date_hierarchy = "fecha_publicacion"

    def contenido_preview(self, obj):
        return obj.contenido[:50] + "..." if len(obj.contenido) > 50 else obj.contenido

    contenido_preview.short_description = "Vista previa de contenido"


admin.site.register(Perfil)
