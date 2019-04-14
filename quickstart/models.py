# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

JURUSAN_CHOICES = (
  ('tif','Teknik Informatika'),
  ('si','Sistem Informasi'),
  ('tin','Teknik Industri'),
  ('d3-si','D3 Sistem Informasi'),
)
FAKULTAS_CHOICES = (
  ('FTT','Fakultas Teknik dan Teknologi Informasi'),
  ('FKES','Fakultas Kesehatan'),
)

class Jurusan(models.Model):
  nama_jurusan = models.CharField("Nama Jurusan",max_length=100, blank=True, default='')
  fakultas = models.CharField(choices=FAKULTAS_CHOICES, max_length=100)

  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('created',)

class Mahasiswa(models.Model):
  nim = models.CharField(max_length=100,unique=True)
  nama = models.CharField("Nama Mahasiswa",max_length=100, blank=True, default='')
  aktif = models.BooleanField(default=True)
  alamat = models.TextField(blank=True,null=True)
  jurusan_fk = models.ForeignKey(Jurusan,on_delete=models.CASCADE,null=True)

  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('created',)