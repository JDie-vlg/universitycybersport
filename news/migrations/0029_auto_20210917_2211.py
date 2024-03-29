# Generated by Django 3.1.5 on 2021-09-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0028_auto_20210917_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournaments',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='news.Team', verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='22:11', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='22:11', verbose_name='Время публикации'),
        ),
    ]
