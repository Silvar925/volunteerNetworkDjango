# Generated by Django 4.2.7 on 2024-01-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VNCore', '0009_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizers',
            name='post',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='post',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Должность'),
        ),
    ]
