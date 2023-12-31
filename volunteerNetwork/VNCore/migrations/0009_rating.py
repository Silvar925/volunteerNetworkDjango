# Generated by Django 4.2.7 on 2024-01-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VNCore', '0008_events_address_events_programevent_news_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Название мероприятия')),
                ('university', models.CharField(max_length=50, verbose_name='ВУЗ')),
                ('countEvents', models.IntegerField(verbose_name='ВУЗ')),
                ('alpha', models.IntegerField(verbose_name='ВУЗ')),
                ('omega', models.IntegerField(verbose_name='ВУЗ')),
                ('points', models.IntegerField(verbose_name='ВУЗ')),
            ],
        ),
    ]
