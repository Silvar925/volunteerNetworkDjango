# Generated by Django 4.2.6 on 2024-01-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('personalProfile', '0002_user_delete_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='VNUser',
        ),
    ]