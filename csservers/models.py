import time
from datetime import date

from django.db import models
#from django.template.defaultfilters import slugify
from slugify import slugify
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Server(models.Model):
    server_name = models.CharField("Server name", max_length=30, null=True, blank=True)
    player_count = models.PositiveIntegerField("Игроков на сервере", null=True, blank=True)
    max_players = models.PositiveIntegerField("Максимальное количество игроков", null=True, blank=True)
    map = models.CharField("Карта", max_length=20, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    host = models.CharField("IP", max_length=75)
    server_username = models.CharField("Username", max_length=75)
    secret = models.CharField("Password", max_length=75)
    ssh_port = models.IntegerField("SSH порт", null=True, blank=True)
    server_port = models.IntegerField("Server порт", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.host

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.host}-{self.server_port}')
        super(Server, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("servers_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Сервер"
        verbose_name_plural = "Серверы"
