# Generated by Django 4.2.1 on 2023-06-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclubapi', '0003_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.URLField(default='https://media.istockphoto.com/id/172371649/photo/a-black-ornately-embossed-book-cover.jpg?s=612x612&w=0&k=20&c=S637eupjX2Y1a-nVnF0jl-IDLYJYMyg5vpwMXw2oqOU='),
        ),
    ]
