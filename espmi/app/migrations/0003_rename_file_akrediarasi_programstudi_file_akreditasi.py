# Generated by Django 4.1.9 on 2023-06-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_dokumen_pogram_studi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programstudi',
            old_name='file_akrediarasi',
            new_name='file_akreditasi',
        ),
    ]
