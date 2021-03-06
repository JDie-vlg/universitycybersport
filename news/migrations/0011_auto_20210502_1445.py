# Generated by Django 3.1.5 on 2021-05-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20210502_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='14:45', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='14:45', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True, verbose_name='Курс обучения'),
        ),
    ]
