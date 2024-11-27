from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import UsuarioModelForm
from django.contrib import messages
from .models import Usuario, Descarte, Pontuacao

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()  # Salva o usuário e retorna a instância
            messages.success(request, 'Usuário cadastrado com sucesso')

            if usuario.tipo_usuario == 'DESCARTADOR':
                print("Redirecionando para homeusu")  # Debug
                return redirect('homeusu')
            elif usuario.tipo_usuario == 'CATADOR':
                print("Redirecionando para homecat")  # Debug
                return redirect('homecat')

            # Adiciona mensagem de erro genérico
            messages.error(request, 'Erro ao determinar o tipo de usuário')

            print(f"Dados enviados: {request.POST}")

        else:
            messages.error(request, 'Erro ao cadastrar usuário')
    else:
        form = UsuarioModelForm()

    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)

def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user: 
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválido')

def homeusu(request):
    return render(request, 'homeusu.html')

def homecat(request):
    return render(request, 'homecat.html')

def perfilusu(request):
    return render(request, 'perfilusu.html')

# Create your views here.
