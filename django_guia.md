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

---

## Principais Arquivos de um App Django
- **models.py**: Define os modelos (tabelas do banco de dados).
- **views.py**: Define as views (lógica de requisição/resposta).
- **serializers.py**: (DRF) Serializa dados para APIs REST.
- **urls.py**: Rotas específicas do app.
- **tests.py**: Testes automatizados do app.
- **admin.py**: Configura modelos para o admin do Django.
- **apps.py**: Configurações do app.
- **migrations/**: Scripts de migração do banco de dados.

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
