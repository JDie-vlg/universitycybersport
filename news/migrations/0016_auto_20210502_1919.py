# Generated by Django 3.1.5 on 2021-05-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20210502_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='19:19', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='19:19', verbose_name='Время публикации'),
        ),
    ]
