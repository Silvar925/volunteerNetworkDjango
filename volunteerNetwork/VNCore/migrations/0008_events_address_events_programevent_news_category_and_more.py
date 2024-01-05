# Generated by Django 4.2.7 on 2024-01-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VNCore', '0007_remove_organizers_numberparticipants_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Адресс'),
        ),
        migrations.AddField(
            model_name='events',
            name='programEvent',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Программа мероприятия'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='news',
            name='numberParticipants',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество участников'),
        ),
        migrations.AlterField(
            model_name='events',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='events',
            name='numberParticipants',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество участников'),
        ),
    ]