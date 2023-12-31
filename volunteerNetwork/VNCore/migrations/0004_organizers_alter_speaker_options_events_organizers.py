# Generated by Django 4.2.7 on 2024-01-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VNCore', '0003_speaker_events_speakers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя спикера')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Биография спикера')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/speakers/', verbose_name='Изображение спикера')),
            ],
            options={
                'verbose_name': 'Организатор',
                'verbose_name_plural': 'Организаторы',
            },
        ),
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'Спикер', 'verbose_name_plural': 'Спикеры'},
        ),
        migrations.AddField(
            model_name='events',
            name='organizers',
            field=models.ManyToManyField(blank=True, to='VNCore.organizers', verbose_name='Орагнизаторы'),
        ),
    ]
