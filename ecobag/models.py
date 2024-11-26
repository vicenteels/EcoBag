from django.db import models


TIPO_USUARIO_CHOICES = [
    ('DESCARATADOR', 'Descartador'),
    ('CATADOR', 'Catador'),
]

STATUS_DESCARTE_CHOICES = [
    ('PENDENTE', 'pendente'),
    ('APROVADO', 'aprovado'),
    ('REPROVADO', 'reprovado'),
]

NIVEL_PONTUACAO = [ 
    ('PÉSSIMO', 0),
    ('RUIM', 25),
    ('REGULAR', 50),
    ('BOM', 75),
    ('ÓTIMO', 100),
]

class Usuario(models.Model):
    username = models.CharField(max_length=12, primary_key=True)
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES)
    name = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"
    
class Descarte(models.Model):
    id_descarte = models.IntegerField(primary_key=True, auto_created=True)
    data = models.DateField(blank=False)
    status_descarte = models.CharField(max_length=10, choices=STATUS_DESCARTE_CHOICES)
    nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_usuario} ({self.status_descarte})"
    
class Pontuacao(models.Model):
    id_pontuacao = models.IntegerField(primary_key=True, auto_created=True)
    pontuacao = models.IntegerField(choices=NIVEL_PONTUACAO)
    nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_descarte = models.ForeignKey(Descarte, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_pontuacao


# Create your models here.
