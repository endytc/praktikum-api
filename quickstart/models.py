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

  def __str__(self):
        return self.nama_jurusan

  class Meta:
    ordering = ('created',)

class Mahasiswa(models.Model):
  nim = models.CharField(max_length=100,unique=True)
  nama = models.CharField("Nama Mahasiswa",max_length=100, blank=True, default='')
  aktif = models.BooleanField(default=True)
  alamat = models.TextField(blank=True,null=True)
  jurusan = models.ForeignKey(Jurusan,on_delete=models.CASCADE,null=True)

  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "[%s] %s" % (self.nim,self.nama)

  class Meta:
    ordering = ('created',)

class Matakuliah(models.Model):
  matakuliah = models.CharField("Matakuliah",max_length=100, blank=True, default='')
  sks = models.IntegerField("SKS",blank=False)

  def __str__(self):
    return self.matakuliah
  
class Nilai(models.Model):
  mahasiswa = models.ForeignKey(Mahasiswa,on_delete=models.CASCADE,null=True)
  matakuliah = models.ForeignKey(Matakuliah,on_delete=models.CASCADE,null=True)
  nilai = models.FloatField(blank=False)
  
  