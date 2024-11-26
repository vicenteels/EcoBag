from django.contrib import admin

from .models import Usuario, Descarte, Pontuacao

admin.site.register(Usuario)
admin.site.register(Descarte)
admin.site.register(Pontuacao)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'tipo_usuario', 'name', 'password')

class DescarteAdmin(admin.ModelAdmin):
    list_display = ('id_descarte', 'data', 'status_descarte', 'nome_usuario')

class PontuacaoAdmin(admin.ModelAdmin):
    list_display = ('id_pontuacao', 'pontuacao', 'nome_usuario', 'id_descarte')

# Register your models here.
