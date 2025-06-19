## Objetivo
Treinar python syntax, explorar documentação do django
Explorar recursos do DJANGO
Treinar orientação a objeto
Produzir uma API que talvez possa ser usada no randori-doctor no lugar do supabase
Depender menos do SUPABASE

# 1.1 Crie e ative um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 1.2 Instale o Django
pip install django

# 1.3 Crie o projeto
django-admin startproject {nome do projeto}

# 1.4 Entre no diretório do projeto
cd {nome do projeto}

# 1.5 Crie um app
python manage.py startapp {nome do app}