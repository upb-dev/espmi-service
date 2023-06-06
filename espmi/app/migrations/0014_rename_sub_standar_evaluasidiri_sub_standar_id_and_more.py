# Generated by Django 4.1.9 on 2023-06-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_jenjang_kelompoksatuanmutu_jenjang_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluasidiri',
            old_name='sub_standar',
            new_name='sub_standar_id',
        ),
        migrations.RenameField(
            model_name='indikator',
            old_name='sub_standar',
            new_name='sub_standar_id',
        ),
        migrations.RenameField(
            model_name='satuanmutu',
            old_name='kelompok_satuan_mutu',
            new_name='kelompok_satuan_mutu_id',
        ),
        migrations.RenameField(
            model_name='standar',
            old_name='satuan_mutu',
            new_name='satuan_mutu_id',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='plotting_unit_kerja',
            new_name='plotting_unit_kerja_id',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='standar',
            new_name='standar_id',
        ),
        migrations.RenameField(
            model_name='temuan',
            old_name='sub_standar',
            new_name='sub_standar_id',
        ),
        migrations.RenameField(
            model_name='visitasi',
            old_name='sub_standar',
            new_name='sub_standar_id',
        ),
    ]