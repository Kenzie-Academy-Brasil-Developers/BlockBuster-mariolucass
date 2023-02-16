# Generated by Django 4.1.6 on 2023-02-16 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movieorder",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="orders",
            field=models.ManyToManyField(
                related_name="orders",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movies",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
