# -*- coding: utf-8 -*-

from django.contrib.auth.models import (User, Group)

from rest_framework import serializers

from quickstart.models import (Mahasiswa,Jurusan,Matakuliah, Nilai)


class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()
    jurusan = serializers.SerializerMethodField()

    def get_id(self,mahasiswa):
        return mahasiswa.id
    
    def get_jurusan(self,mahasiswa):
        if mahasiswa.jurusan is not None:
            return mahasiswa.jurusan.nama_jurusan
        else: 
            return ""
    class Meta:
        model = Mahasiswa
        fields = ('__all__')


class JurusanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jurusan
        fields = ('__all__')

class MatakuliahSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.SerializerMethodField()
    def get_id(self,matakuliah):
        return matakuliah.id
        
    class Meta:
        model = Matakuliah
        fields = ('__all__')

class NilaiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nilai
        fields = ('__all__')