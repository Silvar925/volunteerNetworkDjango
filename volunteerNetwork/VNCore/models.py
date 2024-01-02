from django.db import models

class News(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Название носоти")
    text = models.TextField(blank=True, null=True, verbose_name = "Описание новости")
    photo = models.ImageField(upload_to='images/news/', verbose_name="Изображение", null=True, blank=True)

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Speaker(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя спикера")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография спикера")
    photo = models.ImageField(upload_to='images/speakers/', verbose_name="Изображение спикера", null=True, blank=True)


    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры" 

    def __str__(self):
        return self.name

class Organizers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя организатора")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография орагнизатора")
    photo = models.ImageField(upload_to='images/speakers/', verbose_name="Изображение спикера", null=True, blank=True)


    class Meta:
        verbose_name = "Организатор"
        verbose_name_plural = "Организаторы" 

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название мероприятия")
    text = models.TextField(blank = True, null = True, verbose_name = "Описание новости")
    photo = models.ImageField(upload_to='images/events/', verbose_name="Изображение", null=True, blank=True)

    speakers = models.ManyToManyField(Speaker, blank=True, verbose_name="Спикеры")
    organizers = models.ManyToManyField(Organizers, blank=True, verbose_name="Орагнизаторы")

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"