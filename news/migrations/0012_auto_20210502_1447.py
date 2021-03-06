# Generated by Django 3.1.5 on 2021-05-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20210502_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default='14:47', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.TimeField(default='14:47', verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/user_avatars', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
