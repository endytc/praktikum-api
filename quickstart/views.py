from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from quickstart.serializers import (MahasiswaSerializer,JurusanSerializer,MatakuliahSerializer,NilaiSerializer)
from quickstart.models import (Mahasiswa,Jurusan,Matakuliah,Nilai)

from rest_framework.authentication import (SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated

class PenjumlahanView(APIView):
  def post(self, request):
    angka1 = request.data.get('angka1')
    angka2 = request.data.get('angka2')
    hasil = angka1 + angka2
    data = {
      "hasil": hasil
    }
    return Response(data,status=200)
import sys
class PertamaView(APIView):
  authentication_classes = (TokenAuthentication,
                              BasicAuthentication)
  permission_classes = (IsAuthenticated,)
  
  def get(self, request):
    data = {
      "data":"Halo",
      'user': str(request.user),  # `django.contrib.auth.User` instance.
      'auth': str(request.auth),  # None
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

class MahasiswaViewSet(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,
                            SessionAuthentication,
                            BasicAuthentication)
  permission_classes = (IsAuthenticated,)
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Mahasiswa.objects.all()
  serializer_class = MahasiswaSerializer

  def get_nilai(self,request):
    return Response({"asdf":"asdf"},200)

  '''
    {
      "nim":"",
      "matakuliah_id":"",
      "nilai":""
    }
  '''
  def post_nilai(self,request):
    mahasiswa = Mahasiswa.objects.filter(nim=request.data.get("nim")).first()
    matakuliah = Matakuliah.objects.get(pk=request.data.get("matakuliah_id"))

    nilai = Nilai.objects.filter(mahasiswa=mahasiswa,matakuliah=matakuliah).first()
    if nilai is None:
      nilai = Nilai()
    nilai.mahasiswa = mahasiswa
    nilai.matakuliah = matakuliah
    nilai.nilai = request.data.get("nilai")
    action = nilai.save()

    print(action)
    
    return Response({"message":"ini method post nilai","status":True},200)

class JurusanViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Jurusan.objects.all()
  serializer_class = JurusanSerializer

class MatakuliahViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Matakuliah.objects.all()
  serializer_class = MatakuliahSerializer

class NilaiViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Nilai.objects.all()
  serializer_class = NilaiSerializer
