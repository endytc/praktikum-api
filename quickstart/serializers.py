# -*- coding: utf-8 -*-

from django.contrib.auth.models import (User, Group)

from rest_framework import serializers

from quickstart.models import Mahasiswa


class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mahasiswa
        fields = ('__all__')
