import time
from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    nickname = models.CharField("Никнейм", max_length=30, null=True, unique=True)
    age = models.DecimalField('Возраст', max_digits=2, decimal_places=0, null=True, blank=True)
    about = models.TextField('О себе', max_length=1000, null=True, blank=True)
    avatar = models.ImageField('Аватар', default='default/player-no-avatar.png', upload_to='media/user_avatars')
    city = models.CharField('Город', max_length=25, null=True, blank=True)
    university = models.CharField('Университет', max_length=100, null=True, blank=True)
    group = models.CharField('Учебная группа', max_length=50, null=True, blank=True)
    course = models.DecimalField('Курс обучения', max_digits=1, decimal_places=0, null=True, blank=True)
    birthday = models.DateField('Дата рождения',null=True, blank=True)
    team = models.ForeignKey(
        'Team', verbose_name='команда', on_delete=models.SET_NULL, null=True, blank=True
    )
    role = models.ForeignKey(
        'Role', verbose_name='роль', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)
        if self._state.adding is True:
            Profile.objects.create()

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"slug": self.nickname})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Role(models.Model):
    name = models.CharField('Роль', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Game(models.Model):
    name = models.CharField('Игра', max_length=100)
    icon = models.ImageField('Иконка игры', upload_to="icon_game/", null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)


class News(models.Model):
    title = models.CharField("Название новости", max_length=75)
    text = models.TextField("Содержание")
    image_list = models.ImageField("Изображение", upload_to="news_images/list")
    image_news = models.ImageField("Изображение", upload_to="news_images/news")
    categories = models.ForeignKey(
        Category, verbose_name="категория", on_delete=models.SET_NULL, null=True
    )
    publish_date = models.DateField("Дата публикации", default=date.today)
    publish_time = models.TimeField("Время публикации", default=time.strftime('%H:%M'))
    delay_publication = models.DateTimeField('Когда опубликовать', null=True, blank=True)
    author = models.ForeignKey(
        User, verbose_name="автор", related_name="news_author", on_delete=models.CASCADE, null=True, blank=True
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'({self.title}-{self.publish_date}-{self.publish_time})')
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})

    def get_comments(self):
        return self.comments_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Comments(models.Model):
    text = models.TextField("Сообщение", max_length=1000)
    user = models.ForeignKey(
        User, verbose_name='пользователь', on_delete=models.CASCADE, blank=True, null=True
    )
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    news = models.ForeignKey(News, verbose_name="новость", on_delete=models.CASCADE)
    date = models.DateField("Дата публикации", default=date.today)
    time = models.TimeField("Время публикации", default=time.strftime('%H:%M'))

    def __str__(self):
        return f'{self.user} - {self.news}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Team(models.Model):
    name = models.CharField('Название', max_length=35, unique=True)
    tag = models.CharField('Тег', max_length=16, unique=True)
    logo = models.ImageField('Лого', upload_to="teams_logo/", null=True)
    game = models.ForeignKey(
        Game, verbose_name='игра', on_delete=models.SET_NULL, null=True, blank=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class Key(models.Model):
    team = models.OneToOneField(Team, on_delete=models.SET_NULL, null=True, blank=True)
    key = models.CharField('Код вступления', max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return self.key


class Tournaments(models.Model):
    name = models.CharField('Название турнира', max_length=50)
    description = models.TextField('Описание турнира')
    prize = models.TextField('Призовой')
    game = models.ForeignKey(
        Game, verbose_name='Дисциплина', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, verbose_name='пользователь', on_delete=models.CASCADE, blank=True, null=True
    )
    image = models.ImageField('Лого турнира')
    max_teams = models.PositiveSmallIntegerField('Максимальное количество команд', default=0)
    start_date = models.DateTimeField("Дата начала")
    start_registration_date = models.DateTimeField("Начало регистрации")
    end_registration_date = models.DateTimeField("Конец регистрации")
    slug = models.SlugField(unique=True, blank=True, null=True)
    status = models.BooleanField('Статус активности', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tournament_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name} - {self.game}')
        super(Tournaments, self).save(*args, **kwargs)

    def get_tournament(self):
        return self.tournamentregistration_set

    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"


class TournamentRegistration(models.Model):
    tournaments = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name='пользователь', on_delete=models.CASCADE, blank=True, null=True
    )
