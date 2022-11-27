# Generated by Django 3.1.5 on 2021-05-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20210506_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='about',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='О команду'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='10:02', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='10:02', verbose_name='Время публикации'),
        ),
    ]