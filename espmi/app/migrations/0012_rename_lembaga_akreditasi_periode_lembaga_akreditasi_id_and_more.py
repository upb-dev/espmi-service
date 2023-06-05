# Generated by Django 4.1.9 on 2023-06-05 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_akreditas_programstudi_akreditasi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periode',
            old_name='lembaga_akreditasi',
            new_name='lembaga_akreditasi_id',
        ),
        migrations.RenameField(
            model_name='periode',
            old_name='standar_nasional',
            new_name='standar_nasional_id',
        ),
        migrations.RenameField(
            model_name='periode',
            old_name='tahun',
            new_name='tahun_id',
        ),
        migrations.RenameField(
            model_name='programstudi',
            old_name='akreditasi',
            new_name='akreditasi_type',
        ),
    ]