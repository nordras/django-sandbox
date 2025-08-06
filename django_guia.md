# Guia Rápido Django

## O que é Django?
Django é um framework web em Python para desenvolvimento rápido, seguro e escalável de aplicações web.

---

## Estrutura Básica de um Projeto Django

- **manage.py**: Script para comandos administrativos do projeto (rodar servidor, migrações, criar superusuário, etc).
- **settings.py**: Arquivo de configuração do projeto (apps instalados, banco de dados, idioma, etc).
- **urls.py**: Define as rotas principais do projeto.
- **wsgi.py/asgi.py**: Pontos de entrada para servidores web.
- **apps/**: Diretórios dos apps Django (cada app é um módulo funcional independente).

---

## O que é um App Django?
Um app é um componente modular do projeto, responsável por uma funcionalidade específica (ex: blog, api, autenticação, etc).
Django follows the MVT design pattern (Model View Template).

Model - The data you want to present, usually data from a database.
View - A request handler that returns the relevant template and content - based on the request from the user.
Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

---

## Principais Arquivos de um App Django
manage.py: Script para executar comandos administrativos do Django (migrações, servidor, shell, etc).
settings.py: Configurações do projeto (banco de dados, apps instalados, templates, etc).
urls.py: Mapeamento de URLs para views.
wsgi.py: Interface para servidores web (produção).
apps.py: Configuração da aplicação (nome, auto_field, etc).
models.py: Definição das estruturas de dados (tabelas do banco).
views.py: Lógica das páginas e APIs (controllers).
admin.py: Configuração do painel administrativo.
tests.py: Testes automatizados da aplicação.
migrations/: Histórico de migrações do banco de dados.
templates/: Arquivos HTML para renderização das páginas.
static/: Arquivos estáticos (CSS, JS, imagens).

## Fluxo Básico
Modelos: Definem as tabelas do banco de dados.
Views: Recebem requisições, processam dados e retornam respostas.
Templates: Renderizam o HTML para o usuário.
URLs: Roteiam as requisições para as views corretas.
Admin: Interface administrativa para gerenciar dados.
---

## O que são Modelos?
Modelos são classes Python que representam tabelas do banco de dados. Cada atributo da classe vira uma coluna.

Exemplo:
```python
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicado_em = models.DateField()
```

---

## Comandos Úteis
- `python manage.py makemigrations` — Cria scripts de migração para alterações nos modelos.
- `python manage.py migrate` — Aplica as migrações ao banco de dados.
- `python manage.py runserver` — Inicia o servidor de desenvolvimento.
- `python manage.py createsuperuser` — Cria um usuário admin.


---

## Dicas
- Sempre adicione seus apps em `INSTALLED_APPS` no `settings.py`.
- Use o admin do Django para gerenciar dados facilmente.
- O Django REST Framework (DRF) facilita a criação de APIs REST.

---

Para mais detalhes, consulte a documentação oficial: https://docs.djangoproject.com/pt-br/stable/
