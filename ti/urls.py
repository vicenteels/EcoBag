from django.contrib import admin
from django.urls import path
from ecobag.views import index, cadastro, login, homecat, homeusu, perfilusu, aprovar_reprovar_descarte, solicitacoes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('homecat/', homecat, name='homecat'),
    path('homedesc/', homeusu, name='homeusu'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfilusu, name='perfilusu'),
    path('aprovar_reprovar_descarte/<int:id_descarte>/', aprovar_reprovar_descarte, name='aprovar_reprovar_descarte'),
    path('solicitacoes/', solicitacoes, name='solicitacoes')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)