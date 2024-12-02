from django.shortcuts import render, redirect, get_object_or_404
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
    # Filtra os descartes com status 'PENDENTE', ordenados pela data
    descartes_pendentes = Descarte.objects.filter(status_descarte='PENDENTE').order_by('data')

    return render(request, 'homecat.html', {'descartes_pendentes': descartes_pendentes})

# @login_required(login_url='login/')


def perfilusu(request):
    if request.method == 'POST':
        username_atual = request.POST.get('username')  # Obtém o nome de usuário do formulário
        data = request.POST.get('data')  # Obtém a data do formulário

        # Obtém o nome de usuário da sessão
        username_sessao = request.session.get('username')

        # Verifica se o nome de usuário da sessão corresponde ao nome de usuário do formulário
        if username_sessao == username_atual:
            try:
                usuario_atual = Usuario.objects.get(username=username_atual)  # Busca o usuário no banco de dados

                # Cria uma nova solicitação de descarte
                novo_descarte = Descarte(nome_usuario=usuario_atual, data=data)
                novo_descarte.save()
                messages.success(request, "Sua solicitação de descarte foi criada com sucesso!")
            except Usuario.DoesNotExist:
                messages.error(request, "Usuário não encontrado.")
        else:
            messages.error(request, "O nome de usuário informado não corresponde ao nome de usuário da sessão.")

    return render(request, 'perfilusu.html')  # Redireciona para a página de perfil do usuário

def aprovar_reprovar_descarte(request, id_descarte):
    if request.method == 'POST':
        acao = request.POST.get('acao')
        descarte = get_object_or_404(Descarte, id_descarte=id_descarte)
        
        if acao == 'aprovar':
            descarte.status_descarte = 'APROVADO'
            descarte.nome_usuario.pontuacao_total += 100
        elif acao == 'reprovar':
            descarte.status_descarte = 'REPROVADO'
        
        descarte.save()
        descarte.nome_usuario.save()  # Salva as alterações na pontuação do usuário

        # Redireciona de volta para a página do catador
        return redirect('homecat')  # Certifique-se de que 'homecat' é o nome correto da URL

    return redirect('homecat')
# Create your views here.
