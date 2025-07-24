# Django LeetCode Algorithms API

Uma API Django REST que implementa algoritmos clássicos do LeetCode com documentação Swagger completa e exemplos didáticos de sintaxe Python/Django.

## 🎯 Objetivo

- **Treinar sintaxe Python**: Exemplos abrangentes de conceitos Python básicos e avançados
- **Explorar Django**: Implementação de APIs REST com Django REST Framework
- **Algoritmos LeetCode**: Implementações didáticas com métricas de performance
- **Documentação**: Swagger/OpenAPI para documentação interativa
- **Referência educativa**: Serve como guia de melhores práticas

## 🚀 Endpoints Implementados

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

### 3. Acesse a Documentação

- **Swagger UI**: http://localhost:8000/api/docs/
- **API Reference**: [API_REFERENCE.md](./API_REFERENCE.md)

## 🧪 Testando os Endpoints

### PowerShell (Windows)
```powershell
# Hello World - Referência de sintaxe
Invoke-RestMethod -Uri "http://localhost:8000/api/hello/" -Method GET

# Two Sum
$body = @{ nums = @(2, 7, 11, 15); target = 9 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/api/two-sum/" -Method POST -Body $body -ContentType "application/json"
```

### cURL (Linux/Mac)
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
├── randori_doctor_api/     # App principal
│   ├── models.py          # Modelos Django
│   ├── serializers.py     # Serializers DRF
│   ├── views.py           # Views dos algoritmos
│   └── urls.py            # URLs do app
├── settings.py            # Configurações Django
├── urls.py                # URLs principais
├── manage.py              # Script de gerenciamento
├── API_REFERENCE.md       # Documentação detalhada
└── readme.md             # Este arquivo
```

## 💡 Principais Características

- ✅ **Algoritmos LeetCode**: Two Sum, Add Two Numbers
- ✅ **Documentação Swagger**: Interface interativa para testes
- ✅ **Validação robusta**: Usando Django REST Framework serializers
- ✅ **Métricas de performance**: Tempo de execução e complexidade
- ✅ **Exemplos educativos**: Sintaxe Python/Django completa
- ✅ **Tratamento de erros**: Respostas HTTP apropriadas
- ✅ **Código limpo**: Seguindo melhores práticas Django

## 🎓 Casos de Uso

1. **Aprendizado**: Referência de sintaxe Python e Django
2. **Algoritmos**: Implementações didáticas de problemas LeetCode
3. **API Design**: Exemplo de API REST bem documentada
4. **Testes**: Ambiente para experimentar com Django REST Framework

---

*Desenvolvido como ferramenta educativa para algoritmos e Django*