# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from quickstart.models import (Mahasiswa,Jurusan, Nilai, Matakuliah)
# Register your models here.
class MahasiswaAdmin(admin.ModelAdmin):
  list_display = ['nim','nama','jurusan','aktif','created']

class JurusanAdmin(admin.ModelAdmin):
  list_display = ['nama_jurusan','fakultas']

class MatakuliahAdmin(admin.ModelAdmin):
  list_display = ['matakuliah','sks']

class NilaiAdmin(admin.ModelAdmin):
  list_display = ['matakuliah','mahasiswa','nilai']

admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Jurusan,JurusanAdmin)
admin.site.register(Matakuliah,MatakuliahAdmin)
admin.site.register(Nilai,NilaiAdmin)
