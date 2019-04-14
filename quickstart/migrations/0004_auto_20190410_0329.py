# Generated by Django 2.1.3 on 2019-04-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20190410_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jurusan', models.CharField(blank=True, default='', max_length=100, verbose_name='Nama Jurusan')),
                ('fakultas', models.CharField(choices=[('FTT', 'Fakultas Teknik dan Teknologi Informasi'), ('FKES', 'Fakultas Kesehatan')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.RemoveField(
            model_name='mahasiswa',
            name='fakultas',
        ),
    ]