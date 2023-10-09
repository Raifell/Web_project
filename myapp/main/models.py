from django.db import models


class Book(models.Model):
    name = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=50)
    genre = models.CharField('Жанр', max_length=50)
    pages = models.IntegerField('Количество страниц')
    rang = models.CharField('Возрастной рейтинг', max_length=50)
    article = models.IntegerField('Артикул')

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.name, self.author)


class User(models.Model):
    f_name = models.CharField('Имя', max_length=50)
    s_name = models.CharField('Фамилия', max_length=50)
    n_name = models.CharField('Ник-Нейм', max_length=50)
    email = models.CharField('Почта', max_length=100)
    age = models.IntegerField('Возраст')
    favorite = models.IntegerField('Предпочтения')

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.id, self.f_name, self.s_name, self.n_name, self.age, self.email)
