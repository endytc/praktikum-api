# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from quickstart.models import (Mahasiswa,Jurusan)
# Register your models here.
class MahasiswaAdmin(admin.ModelAdmin):
  list_display = ['nim','nama','aktif','created']

class JurusanAdmin(admin.ModelAdmin):
  list_display = ['nama_jurusan','fakultas']

admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Jurusan,JurusanAdmin)
