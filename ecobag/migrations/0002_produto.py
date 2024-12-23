# Generated by Django 5.1.1 on 2024-12-03 22:14

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecobag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome de Produto')),
                ('valor_pontos', models.IntegerField(verbose_name='Valor em pontos')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='', variations={'thumb': (124, 124)}, verbose_name='Imagem do Produto')),
            ],
        ),
    ]
