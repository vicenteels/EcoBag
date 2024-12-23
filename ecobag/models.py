from django.db import models
from stdimage.models import StdImageField


TIPO_USUARIO_CHOICES = [
    ('DESCARTADOR', 'Descartador'),
    ('CATADOR', 'Catador'),
]

STATUS_DESCARTE_CHOICES = [
    ('PENDENTE', 'pendente'),
    ('APROVADO', 'aprovado'),
    ('REPROVADO', 'reprovado'),
]

class Usuario(models.Model):
    username = models.CharField(max_length=12, primary_key=True)
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES)
    name = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=100, blank=False)
    pontuacao_total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"
    
class Descarte(models.Model):
    id_descarte = models.AutoField(primary_key=True)
    data = models.DateField() 
    status_descarte = models.CharField(max_length=10, choices=STATUS_DESCARTE_CHOICES, default='PENDENTE')
    nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_usuario} ({self.status_descarte})"

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField('Nome de Produto', max_length=255, blank=False)
    valor_pontos = models.IntegerField('Valor em pontos', blank=False)
    imagem = StdImageField('Imagem do Produto', upload_to='cadastro_produto', variations={'thumb':(124,124)}) 

    def __str__(self):
        return self.nome
# Create your models here.
