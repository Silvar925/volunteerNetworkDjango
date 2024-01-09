from django.contrib.auth.models import AbstractUser
from django.db import models

class ExtendedUser(AbstractUser):
    name = models.CharField(max_length = 100, verbose_name = "Имя")
    surname = models.CharField(max_length = 100, verbose_name = "Фамилия")
    fathername = models.CharField(max_length = 100, verbose_name = "Отчество")
    dateOfBirth = models.DateField(verbose_name = "Дата рождения")
    education = models.CharField(max_length = 100 ,verbose_name = "Образование")
    specialization = models.CharField(max_lenght = 100, verbose_name = "Специализация")
    aboutMe = models.CharField(max_length = 200, verbose_name = "О себе")

    