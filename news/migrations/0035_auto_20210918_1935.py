# Generated by Django 3.1.5 on 2021-09-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0034_auto_20210918_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='count_registration_teams',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество зарегестрированных команд'),
        ),
    ]