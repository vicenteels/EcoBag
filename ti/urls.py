from django.contrib import admin
from django.urls import path
from ecobag.views import index, cadastro, login, homecat, homeusu, perfilusu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('homecat/', homecat, name='homecat'),
    path('homedesc/', homeusu, name='homeusu'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfilusu, name='perfilusu'),
]
