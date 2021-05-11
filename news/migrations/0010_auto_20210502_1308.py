# Generated by Django 3.1.5 on 2021-05-02 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_auto_20210501_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournaments',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='13:08', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='13:08', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='team',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.game', verbose_name='игра'),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]