from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioModelForm
from django.contrib import messages
from .models import Usuario, Descarte, Produto

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados.')
    else:
        form = UsuarioModelForm()

    form = UsuarioModelForm()

    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username') #captura as informações do login
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


def homeusu(request):
    produtos = Produto.objects.all()  # Busca todos os produtos cadastrados
    return render(request, 'homeusu.html', {'produtos': produtos})

def homecat(request):
    # Filtra os descartes com status 'PENDENTE', ordenados pela data
    descartes_pendentes = Descarte.objects.filter(status_descarte='PENDENTE').order_by('data')

    return render(request, 'homecat.html', {'descartes_pendentes': descartes_pendentes})


def perfilusu(request):
    # Inicializa a pontuação como 0
    pontos = 0

    # Obtém o nome de usuário da sessão
    username_sessao = request.session.get('username')

    if username_sessao:
        try:
            # Busca o usuário no banco de dados usando o nome de usuário da sessão
            usuario = Usuario.objects.get(username=username_sessao)
            pontos = usuario.pontuacao_total  # Obtém a pontuação total do usuário
        except Usuario.DoesNotExist:
            # Se o usuário não for encontrado, você pode definir pontos como 0 ou lidar de outra forma
            pontos = 0

    if request.method == 'POST':
        username_atual = request.POST.get('username')  # Obtém o nome de usuário do formulário
        data = request.POST.get('data')  # Obtém a data do formulário

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
            messages.error(request, "Verfique o apelido informado.")

    # Renderiza o template com a pontuação e outras informações
    return render(request, 'perfilusu.html', {'pontos': pontos})

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
        return redirect('homecat')  

    return redirect('homecat')

def solicitacoes(request):
    # Obtém o usuário da sessão
    username_sessao = request.session.get('username')

    # Filtra os descartes do usuário logado
    descartes_usuario = Descarte.objects.filter(nome_usuario__username=username_sessao).order_by('-id_descarte')

    # Renderiza o template com os descartes associados ao usuário
    return render(request, 'solicitacoes.html', {'descartes_usuario': descartes_usuario})

def editar_excluir_descarte(request, id_descarte):
    # Busca o descarte pelo ID
    descarte = get_object_or_404(Descarte, id_descarte=id_descarte)

    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'editar':
            # Atualiza a data do descarte
            nova_data = request.POST.get('nova_data')
            descarte.data = nova_data
            descarte.save()
            messages.success(request, 'Data do descarte atualizada com sucesso.')

        elif acao == 'excluir':
            # Exclui o descarte
            descarte.delete()
            messages.success(request, 'Descarte excluído com sucesso.')

    # Redireciona para a página de solicitações
    return redirect('solicitacoes')

def trocar_pontos(request):
    usuario_sessao = request.session.get('username')
    
    # Obtenha o usuário usando o campo correto 'username'
    try:
        usuario = Usuario.objects.get(username=usuario_sessao)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuário não encontrado.')
        return redirect('homeusu')

    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'geracao':
            pontos = 150
            if pontos > usuario.pontuacao_total:
                messages.error(request, 'Saldo de pontos insuficiente')
            else:
                usuario.pontuacao_total -= 150
                usuario.save()
                messages.success(request, 'Pontos trocados com sucesso!')

        elif acao == 'fisk':
            pontos = 200
            if pontos > usuario.pontuacao_total:
                messages.error(request, 'Saldo de pontos insuficiente')
            else:
                usuario.pontuacao_total -= 200
                usuario.save()
                messages.success(request, 'Pontos trocados com sucesso!')

        elif acao == 'camelia':
            pontos = 50
            if pontos > usuario.pontuacao_total:
                messages.error(request, 'Saldo de pontos insuficiente')
            else:
                usuario.pontuacao_total -= 50
                usuario.save()
                messages.success(request, 'Pontos trocados com sucesso!')

    return redirect('homeusu')

# Create your views here.
