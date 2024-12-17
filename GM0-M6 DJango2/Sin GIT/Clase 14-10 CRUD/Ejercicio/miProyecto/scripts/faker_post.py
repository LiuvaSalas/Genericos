import os
import django
from faker import Faker
from datetime import timedelta, datetime
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miProyecto.settings")

django.setup()

from miApp.models import Post

faker = Faker()


def generate_posts(n=200):
    posts = []
    for _ in range(n):
        titulo = faker.sentence(nb_words=6)
        contenido = faker.text(max_nb_chars=1000)
        fecha_publicacion = faker.date_time_between(
            start_date="-1y", end_date="now", tzinfo=None
        )

        posts.append(
            Post(
                titulo=titulo, contenido=contenido, fecha_publicacion=fecha_publicacion
            )
        )

    Post.objects.bulk_create(posts)
    print(f"Se generaron {n} publicaciones correctamente.")


if __name__ == "__main__":
    generate_posts()
