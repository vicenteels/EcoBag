from django.db import models


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
    data = models.DateField()  # Não use auto_now_add aqui, pois estamos definindo a data manualmente
    status_descarte = models.CharField(max_length=10, choices=STATUS_DESCARTE_CHOICES, default='PENDENTE')
    nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_usuario} ({self.status_descarte})"


# Create your models here.
