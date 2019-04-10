# Generated by Django 2.1.3 on 2019-04-10 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=100, unique=True)),
                ('nama', models.CharField(blank=True, default='', max_length=100)),
                ('aktif', models.BooleanField(default=True)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('jurusan', models.CharField(choices=[('tif', 'Teknik Informatika'), ('si', 'Sistem Informasi'), ('tin', 'Teknik Industri')], default='python', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
