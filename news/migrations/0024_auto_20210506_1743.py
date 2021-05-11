# Generated by Django 3.1.5 on 2021-05-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20210506_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='17:43', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='17:43', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='end_registration_date',
            field=models.DateTimeField(verbose_name='Конец регистрации'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='start_date',
            field=models.DateTimeField(verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='start_registration_date',
            field=models.DateTimeField(verbose_name='Начало регистрации'),
        ),
    ]