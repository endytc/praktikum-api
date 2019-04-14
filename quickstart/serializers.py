# -*- coding: utf-8 -*-

from django.contrib.auth.models import (User, Group)

from rest_framework import serializers

from quickstart.models import (Mahasiswa,Jurusan)


class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ('__all__')


class JurusanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jurusan
        fields = ('__all__')