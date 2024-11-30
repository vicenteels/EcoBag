from django.shortcuts import render, redirect
from datetime import date
from django.http.response import HttpResponse
from .forms import UsuarioModelForm
from django.contrib import messages
from .models import Usuario, Descarte

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = usuario.password  # Salve a senha sem encriptar, ou use encriptação se necessário
            usuario.save()
            if usuario.tipo_usuario == 'DESCARTADOR':
                return redirect('homeusu')
            elif usuario.tipo_usuario == 'CATADOR':
                return redirect('homecat')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados informados.')
    else:
        form = UsuarioModelForm()

    form = UsuarioModelForm()

    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # Autenticação personalizada
        try:
            user = Usuario.objects.get(username=username, password=senha)
            # Armazena o username na sessão
            request.session['username'] = user.username

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
    if request.method == 'POST':
        username_atual = request.POST.get('username')  # Obtém o nome de usuário do formulário
        data = request.POST.get('data')  # Obtém a data do formulário

        try:
            usuario_atual = Usuario.objects.get(username=username_atual)  # Busca o usuário no banco de dados

            # Cria uma nova solicitação de descarte
            novo_descarte = Descarte(nome_usuario=usuario_atual, data=data)
            novo_descarte.save()
            messages.success(request, "Sua solicitação de descarte foi criada com sucesso!")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")

    return render(request, 'perfilusu.html')  # Redireciona para a página de perfil do usuário


# Create your views here.
