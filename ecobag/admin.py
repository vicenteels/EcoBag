from django.contrib import admin

from .models import Usuario, Descarte

admin.site.register(Usuario)
admin.site.register(Descarte)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'tipo_usuario', 'name', 'password')

class DescarteAdmin(admin.ModelAdmin):
    list_display = ('id_descarte', 'data', 'status_descarte', 'nome_usuario')


# Register your models here.
