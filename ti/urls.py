from django.contrib import admin
from django.urls import path
from ecobag.views import index, cadastro, login, homecat, homeusu, perfilusu, aprovar_reprovar_descarte, solicitacoes, editar_excluir_descarte
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
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('editar_excluir_descarte/<int:id_descarte>/', editar_excluir_descarte, name='editar_excluir_descarte'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)