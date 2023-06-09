# Generated by Django 4.1.9 on 2023-06-04 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_auditor_program_studis_auditor_units'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auditor',
            old_name='jenis_kelamin',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='auditor',
            name='units',
        ),
        migrations.AddField(
            model_name='auditor',
            name='lembaga_akreditasi_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.lembagaakreditasi'),
        ),
        migrations.AddField(
            model_name='auditor',
            name='units_id',
            field=models.ManyToManyField(null=True, to='app.unit'),
        ),
        migrations.AlterField(
            model_name='auditor',
            name='nik',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
