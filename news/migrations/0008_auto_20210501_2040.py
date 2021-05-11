# Generated by Django 3.1.5 on 2021-05-01 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20210501_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.game', verbose_name='команда'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='20:40', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='20:40', verbose_name='Время публикации'),
        ),
    ]
