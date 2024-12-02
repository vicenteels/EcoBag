from django.contrib import admin
from django.urls import path
from ecobag.views import index, cadastro, login, homecat, homeusu, perfilusu, aprovar_reprovar_descarte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('homecat/', homecat, name='homecat'),
    path('homedesc/', homeusu, name='homeusu'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfilusu, name='perfilusu'),
    path('aprovar_reprovar_descarte/<int:id_descarte>/', aprovar_reprovar_descarte, name='aprovar_reprovar_descarte'),
]
