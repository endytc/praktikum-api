# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from quickstart.models import Mahasiswa
# Register your models here.
class MahasiswaAdmin(admin.ModelAdmin):
  list_display = ['nim','nama','jurusan','aktif','created']

admin.site.register(Mahasiswa, MahasiswaAdmin)
