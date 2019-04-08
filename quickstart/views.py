from rest_framework.views import APIView
from rest_framework.response import Response


class PenjumlahanView(APIView):
  def post(self, request):
    angka1 = request.data.get('angka1')
    angka2 = request.data.get('angka2')
    hasil = angka1 + angka2
    data = {
      "hasil": hasil
    }
    return Response(data,status=200)

class PertamaView(APIView):

  def get(self, request):
    data = {
      "data":"Halo"
    }
    return Response(data,status=200)
  
  def post(self, request):
    data = {
      "data":"Halo ini pake method post"
    }
    return Response(data,status=200)

  def delete(self, request):
    data = {
      "data":"Halo ini pake method delete"
    }
    return Response(data,status=200)
  
  def put(self, request):
    data = {
      "data":"Halo ini pake method put"
    }
    return Response(data,status=200)


class DuaView(APIView):
  def get(self, request):
    data = {
      "data":"Halo ini dari apiview DuaView"
    }
    return Response(data,status=200)
  def post(self, request):
    data = {
      "data":"Halo ini pake method post"
    }
    return Response(data,status=200)

  def delete(self, request):
    data = {
      "data":"Halo ini pake method delete"
    }
    return Response(data,status=200)
  
  def put(self, request):
    data = {
      "data":"Halo ini pake method put"
    }
    return Response(data,status=200)

from rest_framework import viewsets
from quickstart.serializers import (MahasiswaSerializer)
from quickstart.models import Mahasiswa

class MahasiswaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
