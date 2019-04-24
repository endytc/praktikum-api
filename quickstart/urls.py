# -*- coding: utf-8 -*-

from django.urls import path

from quickstart.views import PertamaView
from quickstart.views import DuaView
from quickstart.views import PenjumlahanView
from quickstart.views import (MahasiswaViewSet,JurusanViewSet,MatakuliahViewSet,NilaiViewSet)

from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet)
router.register(r'jurusan', JurusanViewSet)
router.register(r'matakuliah', MatakuliahViewSet)
router.register(r'nilai', NilaiViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('mahasiswa/nilai/save', MahasiswaViewSet.as_view({'post': 'post_nilai'})),
    path('mahasiswa/nilai', MahasiswaViewSet.as_view({'get': 'get_nilai'})),

    path('pertama', PertamaView.as_view()),
    path('dua', DuaView.as_view()),
    path('penjumlahan', PenjumlahanView.as_view()),
    path('penjumlahan', PenjumlahanView.as_view()),
]
