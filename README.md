# ♻️ EcoBag

> **Conectando comunidade e catadores por um futuro mais sustentável.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)


O **EcoBag** é um projeto de Conclusão de Curso Técnico em Informática Integrado ao Ensino Médio do IFSC Xanxerê. Foi desenvolvido para solucionar um problema real da nossa comunidade local: a falta de incentivo na separação correta do lixo reciclável.

Através da gamificação, criamos um ecossistema onde o descarte consciente gera valor, conectando diretamente o **cidadão descartador** e o **catador**, com o apoio de **empresas parceiras**.

## 🌱 Fluxo do Sistema

O sistema gerencia todo o ciclo de incentivo ao descarte correto:

1.  **Solicitação de Etiquetas:** O usuário comum se cadastra e solicita etiquetas identificadoras (ID único vinculado ao seu perfil).
2.  **Descarte Identificado:** O usuário separa seu lixo reciclável, cola sua etiqueta na sacola e registra a **Solicitação de Descarte** no sistema.
3.  **Coleta e Validação:** O catador recebe a sacola, verifica a etiqueta no sistema e avalia o conteúdo.
4.  **Bonificação:**
    * ✅ **Aprovado:** Se a separação estiver correta, o catador valida no sistema e o usuário ganha pontos automaticamente.
    * ❌ **Reprovado:** Se houver mistura de lixo orgânico/incorreto, a validação é negada.
5.  **Recompensa:** O usuário troca seus pontos acumulados por bonificações, descontos ou brindes oferecidos por empresas parceiras cadastradas na plataforma.

##  Funcionalidades

### Para o Usuário (Descartador)
- Cadastro e autenticação segura.
- Solicitação de kit de etiquetas.
- Registro de novos descartes.
- Painel de visualização de pontos (Desconto automático à troca por bonificações).
- Marketplace para troca de pontos.

### Para o Catador 
- Cadastro e autenticação segura.
- Painel de controle de solicitações de descarte.
- Ferramenta de validação de sacolas (Aprovar/Reprovar).

## Tecnologias Utilizadas

- **Backend:** Python 3 + Django 5.1
- **Frontend:** Bootstrap 4, HTML5, CSS3.
- **Banco de Dados:**
    - *Desenvolvimento:* SQLite
    - *Produção:* MySQL
- **Gerenciamento de Dependências:** Pip
- **Variáveis de Ambiente:** Python-Decouple


## Executando o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

### 1. Clone o repositório
```bash
git clone https://github.com/sofii4/ecobag.git

cd ecobag
```


### 2. Crie e ative o ambiente virtual

No Windows (PowerShell ou CMD):

```bash
python -m venv venv
.\venv\Scripts\activate
```

No Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto e adicione o seguinte conteúdo mínimo:

```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
# Caso vá usar MySQL, adicione as variáveis abaixo (opcional)
# DB_NAME=ecobag
# DB_USER=root
# DB_PASSWORD=sua_senha_mysql
# DB_HOST=localhost
# DB_PORT=3306
```

Obs.: Em produção, defina `DEBUG=False` e configure `ALLOWED_HOSTS` adequadamente.

### 5. Prepare o Banco de Dados

Crie as tabelas necessárias:

```bash
python manage.py migrate
```

### 6. Crie um Superusuário (Administrador)

Para acessar o painel administrativo do Django (`/admin`):

```bash
python manage.py createsuperuser
```

### 7. Inicie o Servidor

```bash
python manage.py runserver
```

O projeto estará acessível em: http://127.0.0.1:8000/

## 📌 Nota sobre o Banco de Dados (MySQL | SQLite)

- Padrão (Desenvolvimento): o projeto usa SQLite por padrão para facilitar testes rápidos.
- Produção (MySQL): para usar MySQL, tenha o servidor MySQL em execução e configure as variáveis de ambiente listadas acima. Instale também o conector necessário (ex.: `mysqlclient`).

Exemplo de configuração alternativa:
```py
# settings.py (exemplo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}
```

## 📚 Documentação Acadêmica

Este projeto é o resultado prático de uma pesquisa aprofundada sobre sustentabilidade e realidade local.

Você pode conferir a pesquisa completa, contendo a fundamentação teórica, diagramas UML e a metodologia aplicada, clicando no link abaixo:

📄 **[Trabalho de Conclusão de Curso Completo (PDF)](docs/Trabalho_Integrador_EcoBag.pdf)**

## Agradecimentos

Este projeto foi desenvolvido com foco no impacto social e ambiental, promovendo a reciclagem e apoio aos catadores.

Desenvolvido com carinho,  
Equipe EcoBag 💚♻️