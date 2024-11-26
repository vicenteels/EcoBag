# Generated by Django 5.1.1 on 2024-11-22 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descarte',
            fields=[
                ('id_descarte', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('status_descarte', models.CharField(choices=[('PENDENTE', 'pendente'), ('APROVADO', 'aprovado'), ('REPROVADO', 'reprovado')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('username', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('tipo_usuario', models.CharField(choices=[('DESCARATADOR', 'Descartador'), ('CATADOR', 'Catador')], max_length=12)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id_pontuacao', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('pontuacao', models.IntegerField(choices=[('PÉSSIMO', 0), ('RUIM', 25), ('REGULAR', 50), ('BOM', 75), ('ÓTIMO', 100)])),
                ('id_descarte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecobag.descarte')),
                ('nome_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecobag.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='descarte',
            name='nome_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecobag.usuario'),
        ),
    ]
