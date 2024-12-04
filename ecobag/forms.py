from django import forms
from .models import Usuario, Descarte, Produto

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'tipo_usuario', 'name', 'password']

class DescarteModelForm(forms.ModelForm):
    class Meta:
        model = Descarte
        fields = ['id_descarte', 'data', 'status_descarte', 'nome_usuario']

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['id_produto', 'nome', 'valor_pontos', 'imagem']