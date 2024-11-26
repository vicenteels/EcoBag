from django import forms
from .models import Usuario, Descarte, Pontuacao

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'tipo_usuario', 'name', 'password']

class DescarteModelForm(forms.ModelForm):
    class Meta:
        model = Descarte
        fields = ['id_descarte', 'data', 'status_descarte', 'nome_usuario']

class PontuacaoModelForm(forms.ModelForm):
    class Meta:
        model = Pontuacao
        fields = ['id_pontuacao', 'pontuacao', 'nome_usuario', 'id_descarte']