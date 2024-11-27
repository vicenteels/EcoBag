from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import UsuarioModelForm
from django.contrib import messages
from .models import Usuario, Descarte, Pontuacao

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = usuario.password  # Salve a senha sem encriptar, ou use encriptação se necessário
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            if usuario.tipo_usuario == 'DESCARTADOR':
                return redirect('homeusu')
            elif usuario.tipo_usuario == 'CATADOR':
                return redirect('homecat')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados informados.')
    else:
        form = UsuarioModelForm()

    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # Autenticação personalizada
        try:
            user = Usuario.objects.get(username=username, password=senha)
            if user.tipo_usuario == 'DESCARTADOR':
                return redirect('homeusu')
            elif user.tipo_usuario == 'CATADOR':
                return redirect('homecat')
        except Usuario.DoesNotExist:
            messages.error(request, 'Apelido ou senha inválidos.')
            return redirect('login')

    return render(request, 'login.html')

# @login_required(login_url='login/')
def homeusu(request):
    return render(request, 'homeusu.html')

# @login_required(login_url='login/')
def homecat(request):
    return render(request, 'homecat.html')

# @login_required(login_url='login/')
def perfilusu(request):
    return render(request, 'perfilusu.html')

# Create your views here.
