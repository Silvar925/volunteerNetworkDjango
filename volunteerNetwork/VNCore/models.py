from django.db import models

class News(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Название носоти")
    text = models.TextField(blank=True, null=True, verbose_name = "Описание новости")
    photo = models.ImageField(upload_to='images/news/', verbose_name="Изображение", null=True, blank=True)

    date = models.CharField(max_length = 10, null=True, blank=True, verbose_name = "Дата")
    category = models.CharField(max_length = 20, null=True, blank=True, verbose_name = "Категория")
    numberParticipants = models.IntegerField(null=True, blank=True, verbose_name = "Количество участников")    

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Speaker(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя спикера")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография спикера")
    photo = models.ImageField(upload_to='images/speakers/', verbose_name="Изображение спикера", null=True, blank=True)
    post = models.CharField(max_length=25, blank=True, null=True, verbose_name="Должность")

    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры" 

    def __str__(self):
        return self.name

class Organizers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя организатора")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография орагнизатора")
    photo = models.ImageField(upload_to='images/speakers/', verbose_name="Изображение спикера", null=True, blank=True)
    post = models.CharField(max_length=25, blank=True, null=True, verbose_name="Должность")


    class Meta:
        verbose_name = "Организатор"
        verbose_name_plural = "Организаторы" 

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название мероприятия")
    text = models.TextField(blank = True, null = True, verbose_name = "Описание новости")

    photo = models.ImageField(upload_to='images/events/', verbose_name="Изображение", null=True, blank=True)
    category = models.CharField(max_length = 20, null=True, blank=True, verbose_name = "Категория")
    date = models.CharField(max_length = 10, null=True, blank=True, verbose_name = "Дата")
    numberParticipants = models.IntegerField(null=True, blank=True, verbose_name = "Количество участников")

    address = models.CharField(max_length = 100, null=True, blank=True, verbose_name = "Адресс")
    programEvent = models.CharField(max_length = 100, null=True, blank=True, verbose_name = "Программа мероприятия")

    speakers = models.ManyToManyField(Speaker, blank=True, verbose_name="Спикеры")
    organizers = models.ManyToManyField(Organizers, blank=True, verbose_name="Орагнизаторы")


    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"


class Rating(models.Model):
    fullname = models.CharField(max_length = 50, verbose_name = "ФИО")
    university = models.CharField(max_length = 50, verbose_name = "ВУЗ")
    countEvents = models.IntegerField(verbose_name = "Количество мероприятий")
    alpha = models.IntegerField(verbose_name = "Альфа")
    omega = models.IntegerField(verbose_name = "Омега")
    points = models.IntegerField(verbose_name = "Баллы")

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинг"