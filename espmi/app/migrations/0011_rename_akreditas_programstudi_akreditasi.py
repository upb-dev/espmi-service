# Generated by Django 4.1.9 on 2023-06-05 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_unit_menu_unit_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programstudi',
            old_name='akreditas',
            new_name='akreditasi',
        ),
    ]