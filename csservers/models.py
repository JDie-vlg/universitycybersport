from django.db import models
# from django.template.defaultfilters import slugify
from slugify import slugify
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Server(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    host = models.CharField("IP", max_length=75)
    server_username = models.CharField("Username", max_length=75)
    secret = models.CharField("Password", max_length=75)
    port = models.IntegerField("Порт")
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.host

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.host}')
        super(Server, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("servers_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Сервер"
        verbose_name_plural = "Серверы"
