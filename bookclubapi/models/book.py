from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """Database model for books"""

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.URLField(
        default="https://media.istockphoto.com/id/172371649/photo/a-black-ornately-embossed-book-cover.jpg?s=612x612&w=0&k=20&c=S637eupjX2Y1a-nVnF0jl-IDLYJYMyg5vpwMXw2oqOU="
    )
    synopsis = models.CharField(null=True, max_length=1000)
