# Generated by Django 3.1.5 on 2021-09-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0027_auto_20210917_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournamentregistration',
            options={},
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='20:17', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='20:17', verbose_name='Время публикации'),
        ),
    ]
