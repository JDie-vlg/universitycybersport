# Generated by Django 3.1.5 on 2021-04-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210429_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='22:58', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='22:58', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Возраст'),
        ),
    ]
