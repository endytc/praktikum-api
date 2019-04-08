from django.conf.urls import url
from django.urls import (path,include)
from django.contrib import admin
from quickstart.models import Mahasiswa

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/v1/', include('quickstart.urls')),  
]
