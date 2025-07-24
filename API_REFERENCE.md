# API Reference - Django LeetCode Algorithms

Este projeto implementa endpoints para algoritmos clássicos do LeetCode usando Django REST Framework, servindo como referência didática de sintaxe Python/Django.

## 🚀 Endpoints Disponíveis

### 1. Hello World - Referência de Sintaxe
**GET** `/api/hello/`

Endpoint educativo que retorna exemplos abrangentes de sintaxe Python e Django.

**Conteúdo:**
- ✅ Variáveis e tipos de dados
- ✅ Funções (básicas, lambdas, generators, decorators)
- ✅ Classes (herança, properties, métodos especiais)
- ✅ Estruturas de dados (stacks, queues, defaultdict, heapq)
- ✅ Controle de fluxo (if/else, loops, try/except, match/case)
- ✅ Conceitos avançados (asyncio, type hints, dataclass, enum)
- ✅ Exemplos Django (models, serializers, views, admin, signals)
- ✅ Algoritmos (bubble sort, quick sort, binary search, DFS, BFS)
- ✅ Dicas úteis e melhores práticas

### 2. Two Sum Algorithm
**POST** `/api/two-sum/`

Implementa o algoritmo Two Sum usando HashMap para complexidade O(n).

**Request Body:**
```json
{
  "nums": [2, 7, 11, 15],
  "target": 9
}
```

**Response:**
```json
{
  "algorithm": "Two Sum",
  "input": {
    "nums": [2, 7, 11, 15],
    "target": 9
  },
  "result": [0, 1],
  "description": "Índices 0 e 1 somam 9",
  "explanation": "nums[0] + nums[1] = 2 + 7 = 9",
  "time_complexity": "O(n)",
  "space_complexity": "O(n)",
  "execution_time_ms": 1.23
}
```

**Constraints:**
- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹

### 3. Add Two Numbers Algorithm
**POST** `/api/add-two-numbers/`

Simula soma de linked lists representando números em ordem reversa.

**Request Body:**
```json
{
  "l1": [2, 4, 3],
  "l2": [5, 6, 4]
}
```

**Response:**
```json
{
  "algorithm": "Add Two Numbers",
  "input": {
    "l1": [2, 4, 3],
    "l2": [5, 6, 4]
  },
  "result": [7, 0, 8],
  "description": "342 + 465 = 807",
  "explanation": "Lista [2,4,3] representa 342, lista [5,6,4] representa 465, resultado [7,0,8] representa 807",
  "time_complexity": "O(max(m,n))",
  "space_complexity": "O(max(m,n))",
  "execution_time_ms": 1.45,
  "steps_details": {
    "l1_as_number": 342,
    "l2_as_number": 465,
    "result_as_number": 807,
    "carry_operations": "Processamento com carry bit a bit"
  }
}
```

**Constraints:**
- 1 ≤ número de nós ≤ 100
- 0 ≤ valor do nó ≤ 9

## 📖 Documentação Interativa

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **Schema JSON**: http://localhost:8000/api/schema/

## 🧪 Testando os Endpoints

### PowerShell (Windows)
```powershell
# Hello World
Invoke-RestMethod -Uri "http://localhost:8000/api/hello/" -Method GET

# Two Sum
$body = @{
    nums = @(2, 7, 11, 15)
    target = 9
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/two-sum/" -Method POST -Body $body -ContentType "application/json"

# Add Two Numbers
$body = @{
    l1 = @(2, 4, 3)
    l2 = @(5, 6, 4)
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/add-two-numbers/" -Method POST -Body $body -ContentType "application/json"
```

### cURL (Linux/Mac)
```bash
# Hello World
curl -X GET http://localhost:8000/api/hello/

# Two Sum
curl -X POST http://localhost:8000/api/two-sum/ \
  -H "Content-Type: application/json" \
  -d '{"nums": [2, 7, 11, 15], "target": 9}'

# Add Two Numbers
curl -X POST http://localhost:8000/api/add-two-numbers/ \
  -H "Content-Type: application/json" \
  -d '{"l1": [2, 4, 3], "l2": [5, 6, 4]}'
```

## 🔧 Configuração do Projeto

### Dependências Principais
```
Django>=4.2.0
djangorestframework>=3.14.0
drf-spectacular>=0.26.0
```

### Comandos Úteis
```bash
# Iniciar servidor
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Shell interativo
python manage.py shell

# Testes
python manage.py test
```

## 📚 Recursos Educativos

O endpoint `/api/hello/` serve como uma referência completa de:

1. **Sintaxe Python Básica**: Variáveis, funções, classes, estruturas de dados
2. **Conceitos Avançados**: Asyncio, type hints, decorators, context managers
3. **Django Framework**: Models, serializers, views, admin, signals
4. **Algoritmos**: Ordenação, busca, grafos
5. **Melhores Práticas**: Nomenclatura, organização, performance

## 🎯 Exemplos de Uso

### Aprendendo Sintaxe Python
```python
# Acessar exemplos via API
import requests
response = requests.get("http://localhost:8000/api/hello/")
examples = response.json()["python_syntax_examples"]
print(examples["functions"]["list_comprehension"])
# Output: squares = [x**2 for x in range(10)]
```

### Testando Algoritmos
```python
# Two Sum
import requests
data = {"nums": [3, 2, 4], "target": 6}
response = requests.post("http://localhost:8000/api/two-sum/", json=data)
result = response.json()
print(f"Resultado: {result['result']}")  # [1, 2]
```

## 📈 Performance e Métricas

Todos os endpoints retornam métricas de performance:
- **execution_time_ms**: Tempo de execução em milissegundos
- **time_complexity**: Complexidade temporal do algoritmo
- **space_complexity**: Complexidade espacial do algoritmo

## 🔍 Validação e Tratamento de Erros

- Validação automática de entrada via Django REST Framework serializers
- Mensagens de erro descritivas para entradas inválidas
- Tratamento de exceções com responses HTTP apropriados

## 📝 Notas de Desenvolvimento

Este projeto foi desenvolvido como ferramenta educativa para:
- Demonstrar implementação de APIs REST com Django
- Exemplificar algoritmos clássicos de programação
- Servir como referência de sintaxe Python/Django
- Mostrar boas práticas de documentação API com Swagger

---

*Desenvolvido como referência educativa para algoritmos e sintaxe Python/Django*
