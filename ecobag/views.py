from django.shortcuts import render
# from .forms import UsuarioModelForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    # if request.method == 'POST':
    #     form = UsuarioModelForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Usuario cadastrado com sucesso')
    #     else: 
    #         messages.success(request, 'Erro ao cadastrar usuário')
    # else:
    #     form = UsuarioModelForm()
    #     context = {
    #         'form' : form
    #     }
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def homeusu(request):
    return render(request, 'homeusu.html')

def homecat(request):
    return render(request, 'homecat.html')

def perfilusu(request):
    return render(request, 'perfilusu.html')

# Create your views here.
