# Generated by Django 2.1.3 on 2019-05-05 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='jurusan_fk',
            new_name='jurusan',
        ),
    ]
