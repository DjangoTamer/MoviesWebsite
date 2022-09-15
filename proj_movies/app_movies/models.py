from django.db import models
from django.urls import reverse
from datetime import date

###
class Country(models.Model):
    name = models.CharField('Страна', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=100)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField('URL', max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Person(models.Model):
    OCCUPATIONS = [
        ('A', 'Актер'),
        ('D', 'Режиссер'),
        ('AD', 'Режиссер/Актер'),
    ]
    name = models.CharField('Имя', max_length=100)
    occupation = models.CharField('Деятельность', max_length=2, choices=OCCUPATIONS)
    birth = models.DateField('Дата рождения', blank=True, null=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, verbose_name='Страна')
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField('Фото', upload_to='persons', blank=True)
    slug = models.SlugField('URL', max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person', kwargs={'slug': self.slug})

    def calculate_age(self):
        today = date.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Личности'


class Movie(models.Model):
    name = models.CharField('Имя', max_length=100)
    year = models.PositiveSmallIntegerField('Год')
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, verbose_name='Страна')
    description = models.TextField('Описание')
    cover = models.ImageField('Обложка', upload_to='covers', blank=True)
    genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    director = models.ManyToManyField('Person', verbose_name='Режиссер', related_name='dir')
    actor = models.ManyToManyField('Person', verbose_name='Актер', related_name='act')
    budget = models.PositiveBigIntegerField('Бюджет', default=0)
    box_office = models.PositiveBigIntegerField('Сборы', default=0)
    runtime = models.PositiveSmallIntegerField('Продолжительность', default=0)
    slug = models.SlugField('URL', max_length=100, unique=True, db_index=True)
    published = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.slug})

    def get_main_comments(self):
        return self.comment_set.filter(to_whom__isnull=True)

    def get_secondary_comments(self):
        return self.comment_set.filter(to_whom=self.id)



    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Scene(models.Model):
    name = models.CharField('Сцена', max_length=100)
    photo = models.ImageField('Фото', upload_to='scenes', blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True, verbose_name='Фильм')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'


class Rating(models.Model):
    ip = models.GenericIPAddressField('ip-адрес')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name='Фильм')
    value = models.PositiveSmallIntegerField('Оценка')

    def __str__(self):
        return f'{self.movie} - {self.value}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Comment(models.Model):
    user = models.CharField('Пользователь', max_length=100)
    email = models.EmailField('Почта')
    text = models.TextField('Комментарий')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True, verbose_name='Фильм')
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_update = models.DateTimeField('Дата редактирования', auto_now=True)
    to_whom = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Кому')

    def __str__(self):
        return f'{self.user} - {self.movie} - {self.to_whom_id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'