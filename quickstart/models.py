# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

JURUSAN_CHOICES = (
  ('tif','Teknik Informatika'),
  ('si','Sistem Informasi'),
  ('tin','Teknik Industri')
)

class Mahasiswa(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nim = models.TextField(unique=True)
    nama = models.CharField(max_length=100, blank=True, default='')
    aktif = models.BooleanField(default=True)
    jurusan = models.CharField(choices=JURUSAN_CHOICES, default='python', max_length=100)

    class Meta:
        ordering = ('created',)