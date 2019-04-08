# -*- coding: utf-8 -*-

from django.urls import path

from quickstart.views import PertamaView
from quickstart.views import DuaView
from quickstart.views import PenjumlahanView
from quickstart.views import MahasiswaViewSet

from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('pertama', PertamaView.as_view()),
    path('dua', DuaView.as_view()),
    path('penjumlahan', PenjumlahanView.as_view()),
    path('penjumlahan', PenjumlahanView.as_view()),
]
