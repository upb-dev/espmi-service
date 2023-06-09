# Generated by Django 4.1.9 on 2023-06-06 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_dokuments_evaluasidiri_dokumen_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documenttype',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='dokumen',
            old_name='type_id',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='evaluasidiri',
            old_name='dokumen_id',
            new_name='dokumen',
        ),
        migrations.RenameField(
            model_name='evaluasidiri',
            old_name='indikator_id',
            new_name='indikator',
        ),
        migrations.RenameField(
            model_name='evaluasidiri',
            old_name='sub_standar_id',
            new_name='sub_standar',
        ),
        migrations.RenameField(
            model_name='groupmenurelation',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='groupmenurelation',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='groupsubmenurelation',
            old_name='submenu_id',
            new_name='submenu',
        ),
        migrations.RenameField(
            model_name='indikator',
            old_name='sub_standar_id',
            new_name='sub_standar',
        ),
        migrations.RenameField(
            model_name='kelompoksatuanmutu',
            old_name='jenjang_id',
            new_name='jenjang',
        ),
        migrations.RenameField(
            model_name='kelompoksatuanmutu',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='kelompoksatuanmutu',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='nilaimutu',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='nilaimutu',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='periode',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='periode',
            old_name='standar_nasional_id',
            new_name='standar_nasional',
        ),
        migrations.RenameField(
            model_name='periode',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='rencanatindaklanjut',
            old_name='temuan_id',
            new_name='temuan',
        ),
        migrations.RenameField(
            model_name='satuanmutu',
            old_name='jenjang_id',
            new_name='jenjang',
        ),
        migrations.RenameField(
            model_name='satuanmutu',
            old_name='kelompok_satuan_mutu_id',
            new_name='kelompok_satuan_mutu',
        ),
        migrations.RenameField(
            model_name='satuanmutu',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='satuanmutu',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='standar',
            old_name='jenjang_id',
            new_name='jenjang',
        ),
        migrations.RenameField(
            model_name='standar',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='standar',
            old_name='satuan_mutu_id',
            new_name='satuan_mutu',
        ),
        migrations.RenameField(
            model_name='standar',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='standarnasionalperioderelation',
            old_name='periode_id',
            new_name='periode',
        ),
        migrations.RenameField(
            model_name='standarnasionalperioderelation',
            old_name='standar_nasional_id',
            new_name='standar_nasional',
        ),
        migrations.RenameField(
            model_name='submenu',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='jenjang_id',
            new_name='jenjang',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='plotting_unit_kerja_id',
            new_name='plotting_unit_kerja',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='standar_id',
            new_name='standar',
        ),
        migrations.RenameField(
            model_name='substandar',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='targetnilaimutu',
            old_name='lembaga_akreditasi_id',
            new_name='lembaga_akreditasi',
        ),
        migrations.RenameField(
            model_name='targetnilaimutu',
            old_name='program_studi_id',
            new_name='program_studi',
        ),
        migrations.RenameField(
            model_name='targetnilaimutu',
            old_name='tahun_id',
            new_name='tahun',
        ),
        migrations.RenameField(
            model_name='temuan',
            old_name='sub_standar_id',
            new_name='sub_standar',
        ),
        migrations.RenameField(
            model_name='visitasi',
            old_name='indikator_id',
            new_name='indikator',
        ),
        migrations.RenameField(
            model_name='visitasi',
            old_name='sub_standar_id',
            new_name='sub_standar',
        ),
    ]
