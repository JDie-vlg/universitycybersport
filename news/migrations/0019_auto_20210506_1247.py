# Generated by Django 3.1.5 on 2021-05-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20210506_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='12:47', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='12:47', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='image',
            field=models.ImageField(upload_to='tournaments/', verbose_name='Лого турнира'),
        ),
    ]
