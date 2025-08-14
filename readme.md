# Django Sandbox - Algoritmos & API

Uma plataforma Django completa para treinar algoritmos, sintaxe Python e explorar Django REST Framework com documentação Swagger e interface web interativa.

## 🎯 Objetivos

- **Treinar Algoritmos**: Sandbox interativo para executar algoritmos clássicos
- **Explorar Django**: APIs REST, templates, views e melhores práticas
- **Sintaxe Python**: Exemplos abrangentes de conceitos Python básicos e avançados
- **LeetCode Practice**: Implementações didáticas com métricas de performance
- **DevOps Ready**: Configurado com Docker, Helm, GitHub Actions e Terraform

## 🧪 Sandbox de Algoritmos

### Interface Web Interativa
- **URL**: `http://localhost:8000/sandbox/`
- **Funcionalidade**: Execute algoritmos diretamente na interface
- **Visualização**: Resultados JSON em tempo real

### Algoritmos Implementados

| ID | Nome | Descrição | Dificuldade |
|----|------|-----------|-------------|
| 1 | Two Sum | Encontrar dois números que somam target | Fácil |
| 2 | Reverse String | Inverter uma string | Fácil |
| 3 | Fibonacci | Calcular sequência de Fibonacci | Médio |
| 4 | Binary Search | Busca binária em array ordenado | Médio |
| 5 | Valid Palindrome | Verificar se string é palíndromo | Fácil |
| 6 | Remove Duplicates | Remover duplicatas de array ordenado | Fácil |
| 7 | Merge Sorted Arrays | Combinar dois arrays ordenados | Fácil |
| 8 | Contains Duplicate | Verificar se há duplicatas no array | Fácil |
| 9 | Valid Anagram | Verificar se duas strings são anagramas | Fácil |

## 🚀 Endpoints da API

### Sandbox Interativo
| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/sandbox/` | GET | Interface web dos algoritmos |
| `/sandbox/run/<id>/` | GET | Executar algoritmo específico via API |

### API REST
| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/api/hello/` | GET | Referência completa de sintaxe Python/Django |
| `/api/two-sum/` | POST | Algoritmo Two Sum (LeetCode #1) |
| `/api/add-two-numbers/` | POST | Algoritmo Add Two Numbers (LeetCode #2) |
| `/api/docs/` | GET | Documentação Swagger UI |
| `/api/redoc/` | GET | Documentação ReDoc |
| `/api/schema/` | GET | Schema OpenAPI JSON |

## 📖 Documentação Detalhada

Veja [API_REFERENCE.md](./API_REFERENCE.md) para documentação completa com exemplos de uso.

## ⚡ Quick Start

### 1. Configuração do Ambiente

```bash
# Clone e entre no diretório
cd django-sandbox

# Crie e ative ambiente virtual
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/macOS

# Instale dependências
pip install django djangorestframework drf-spectacular
```

### 2. Execute o Servidor

```bash
# Execute migrações (se necessário)
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

### 3. Acesse as Aplicações

- **Sandbox Interativo**: http://localhost:8000/sandbox/
- **API REST**: http://localhost:8000/api/
- **Swagger UI**: http://localhost:8000/api/docs/
- **API Reference**: [API_REFERENCE.md](./API_REFERENCE.md)

## 🧪 Testando os Algoritmos

### Via Interface Web (Sandbox)
1. Acesse http://localhost:8000/sandbox/
2. Clique em "▶️ Executar" em qualquer algoritmo
3. Veja o resultado JSON na interface

### Via API Direta
```bash
# Testar algoritmo específico por ID
curl http://localhost:8000/sandbox/run/5/   # Valid Palindrome
curl http://localhost:8000/sandbox/run/9/   # Valid Anagram
```

### Via API REST (Endpoints Customizados)
#### PowerShell (Windows)
```powershell
# Hello World - Referência de sintaxe
Invoke-RestMethod -Uri "http://localhost:8000/api/hello/" -Method GET

# Two Sum
$body = @{ nums = @(2, 7, 11, 15); target = 9 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/api/two-sum/" -Method POST -Body $body -ContentType "application/json"
```

#### cURL (Linux/Mac)
```bash
# Hello World
curl -X GET http://localhost:8000/api/hello/

# Two Sum
curl -X POST http://localhost:8000/api/two-sum/ \
  -H "Content-Type: application/json" \
  -d '{"nums": [2, 7, 11, 15], "target": 9}'
```

## 📚 Recursos Educativos

O endpoint `/api/hello/` inclui exemplos de:

- **Python Básico**: Variáveis, funções, classes, controle de fluxo
- **Python Avançado**: Decorators, generators, asyncio, type hints
- **Django**: Models, serializers, views, admin, signals
- **Algoritmos**: Sorting, searching, graph traversal
- **Melhores práticas**: Nomenclatura, organização, performance

## 🔧 Estrutura do Projeto

```
django-sandbox/
├── .github/workflows/      # GitHub Actions CI/CD
├── charts/                 # Helm charts para Kubernetes
├── infra/                  # Scripts Terraform/OpenTofu
├── sandbox/                # App do sandbox interativo
│   ├── templates/         # Templates HTML
│   ├── views.py          # Algoritmos e views
│   ├── models.py         # Modelos Django
│   └── urls.py           # URLs do sandbox
├── randori_doctor_api/     # API REST principal
│   ├── models.py          # Modelos Django
│   ├── serializers.py     # Serializers DRF
│   ├── views.py           # Views dos algoritmos
│   └── urls.py            # URLs da API
├── Dockerfile              # Container Docker
├── requirements.txt        # Dependências Python
├── settings.py            # Configurações Django
├── urls.py                # URLs principais
├── manage.py              # Script de gerenciamento
├── API_REFERENCE.md       # Documentação detalhada
└── readme.md             # Este arquivo
```

## 🐳 DevOps & Deploy

### Docker
```bash
# Build da imagem
docker build -t django-sandbox:latest .

# Executar container
docker run -p 8000:8000 django-sandbox:latest
```

### Kubernetes com Helm
```bash
# Deploy no cluster
helm install django-sandbox ./charts/django-sandbox

# Upgrade
helm upgrade django-sandbox ./charts/django-sandbox
```

### GitHub Actions
- **CI**: Testes automatizados e build Docker
- **CD**: Deploy automatizado via Helm
- **Integração**: Jenkins para pipelines complexos

## 💡 Principais Características

- ✅ **Sandbox Interativo**: Interface web para executar algoritmos
- ✅ **9 Algoritmos**: Two Sum, Fibonacci, Palindrome, Binary Search, etc.
- ✅ **API REST**: Endpoints customizados com DRF
- ✅ **Documentação Swagger**: Interface interativa para testes
- ✅ **DevOps Ready**: Docker, Helm, GitHub Actions, Terraform
- ✅ **Validação robusta**: Usando Django REST Framework serializers
- ✅ **Interface moderna**: Templates HTML responsivos
- ✅ **Exemplos educativos**: Sintaxe Python/Django completa
- ✅ **Tratamento de erros**: Respostas HTTP apropriadas
- ✅ **Código limpo**: Seguindo melhores práticas Django

## 🎓 Casos de Uso

1. **Aprendizado**: Referência de sintaxe Python e Django
2. **Algoritmos**: Sandbox para testar implementações
3. **API Design**: Exemplo de API REST bem documentada
4. **DevOps**: Pipeline completo CI/CD com Kubernetes
5. **Prototipagem**: Base para experimentos Django

---

*Plataforma completa para algoritmos, Django e DevOps - do desenvolvimento ao deploy em Kubernetes*