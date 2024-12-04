from django.contrib import admin

from .models import Usuario, Descarte, Produto

admin.site.register(Usuario)
admin.site.register(Descarte)
admin.site.register(Produto)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'tipo_usuario', 'name', 'password')

class DescarteAdmin(admin.ModelAdmin):
    list_display = ('id_descarte', 'data', 'status_descarte', 'nome_usuario')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id_produto', 'nome', 'valor_pontos', 'imagem')


# Register your models here.
