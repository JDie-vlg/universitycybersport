# Generated by Django 3.1.5 on 2021-05-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20210506_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='16:34', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='16:34', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
