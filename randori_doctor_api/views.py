from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Room, Leader, Participant, Session
from .serializers import (
    RoomSerializer, LeaderSerializer, ParticipantSerializer, SessionSerializer,
    TwoSumSerializer, TwoSumResponseSerializer, AddTwoNumbersSerializer
)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class LeaderViewSet(viewsets.ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

@extend_schema(
    description="Endpoint Hello World e exemplos de sintaxe Python e Django",
    summary="Hello World e Exemplos de Sintaxe",
    responses={
        200: {
            "type": "object",
            "properties": {
                "message": {"type": "string", "example": "Hello World!"},
                "status": {"type": "string", "example": "success"},
                "framework_info": {
                    "type": "object",
                    "properties": {
                        "framework": {"type": "string", "example": "Django REST Framework"},
                        "version": {"type": "string", "example": "1.0.0"},
                        "description": {"type": "string", "example": "Meu primeiro endpoint Django!"}
                    }
                },
                "python_syntax_examples": {
                    "type": "object",
                    "properties": {
                        "variables": {"type": "object"},
                        "functions": {"type": "object"},
                        "classes": {"type": "object"},
                        "data_structures": {"type": "object"}
                    }
                }
            }
        }
    },
    tags=["Hello World"]
)
@api_view(['GET'])
def hello_world(request):
    """Endpoint Hello World e exemplos de sintaxe Python e Django"""
    return Response({
        'message': 'Hello World!',
        'status': 'success',
        'framework_info': {
            'framework': 'Django REST Framework',
            'version': '1.0.0',
            'description': 'Meu primeiro endpoint Django!'
        },
        'python_syntax_examples': {
            'variables': {
                'string': 'name = "Python"',
                'integer': 'age = 25',
                'float': 'pi = 3.14159',
                'boolean': 'is_active = True',
                'list': 'numbers = [1, 2, 3, 4, 5]',
                'dict': 'person = {"name": "João", "age": 30}',
                'tuple': 'coordinates = (10, 20)',
                'set': 'unique_numbers = {1, 2, 3, 4, 5}',
                'none': 'result = None',
                'multiple_assignment': 'x, y, z = 1, 2, 3',
                'unpacking': 'a, *rest, b = [1, 2, 3, 4, 5]'
            },
            'functions': {
                'basic_function': 'def greet(name):\n    return f"Hello, {name}!"',
                'function_with_default': 'def power(base, exponent=2):\n    return base ** exponent',
                'args_kwargs': 'def flexible_func(*args, **kwargs):\n    return args, kwargs',
                'lambda': 'square = lambda x: x ** 2',
                'lambda_with_filter': 'evens = list(filter(lambda x: x % 2 == 0, range(10)))',
                'list_comprehension': 'squares = [x**2 for x in range(10)]',
                'dict_comprehension': 'squares_dict = {x: x**2 for x in range(5)}',
                'generator': 'def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b',
                'generator_expression': 'squares_gen = (x**2 for x in range(10))',
                'closure': 'def outer(x):\n    def inner(y):\n        return x + y\n    return inner',
                'decorator': '@property\n@staticmethod\n@classmethod\ndef my_decorator(func):\n    def wrapper(*args, **kwargs):\n        print("Before")\n        result = func(*args, **kwargs)\n        print("After")\n        return result\n    return wrapper'
            },
            'classes': {
                'basic_class': 'class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def introduce(self):\n        return f"Hi, I\'m {self.name}"',
                'inheritance': 'class Student(Person):\n    def __init__(self, name, age, course):\n        super().__init__(name, age)\n        self.course = course',
                'property': 'class Circle:\n    def __init__(self, radius):\n        self._radius = radius\n    \n    @property\n    def area(self):\n        return 3.14159 * self._radius ** 2',
                'class_methods': 'class MyClass:\n    count = 0\n    \n    @classmethod\n    def get_count(cls):\n        return cls.count\n    \n    @staticmethod\n    def utility_func():\n        return "Static method"',
                'dunder_methods': 'class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    \n    def __str__(self):\n        return f"Point({self.x}, {self.y})"\n    \n    def __add__(self, other):\n        return Point(self.x + other.x, self.y + other.y)',
                'context_manager': 'class FileManager:\n    def __init__(self, filename, mode):\n        self.filename = filename\n        self.mode = mode\n    \n    def __enter__(self):\n        self.file = open(self.filename, self.mode)\n        return self.file\n    \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        self.file.close()'
            },
            'data_structures': {
                'stack': 'stack = []\nstack.append(1)  # push\nitem = stack.pop()  # pop',
                'queue': 'from collections import deque\nqueue = deque()\nqueue.append(1)  # enqueue\nitem = queue.popleft()  # dequeue',
                'dictionary_operations': 'data = {}\ndata["key"] = "value"\nvalue = data.get("key", "default")',
                'set_operations': 'set1 = {1, 2, 3}\nset2 = {3, 4, 5}\nunion = set1 | set2\nintersection = set1 & set2',
                'defaultdict': 'from collections import defaultdict\ndd = defaultdict(list)\ndd["key"].append("value")',
                'counter': 'from collections import Counter\ncounts = Counter("hello world")',
                'namedtuple': 'from collections import namedtuple\nPoint = namedtuple("Point", ["x", "y"])\np = Point(1, 2)',
                'heapq': 'import heapq\nheap = [3, 1, 4, 1, 5]\nheapq.heapify(heap)\nsmallest = heapq.heappop(heap)'
            },
            'control_flow': {
                'if_statement': 'if age >= 18:\n    print("Adult")\nelif age >= 13:\n    print("Teenager")\nelse:\n    print("Child")',
                'for_loop': 'for i in range(5):\n    print(f"Number: {i}")',
                'for_enumerate': 'for index, value in enumerate(["a", "b", "c"]):\n    print(f"{index}: {value}")',
                'for_zip': 'for x, y in zip([1, 2, 3], ["a", "b", "c"]):\n    print(f"{x}: {y}")',
                'while_loop': 'count = 0\nwhile count < 5:\n    print(count)\n    count += 1',
                'try_except': 'try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")\nfinally:\n    print("Cleanup")',
                'with_statement': 'with open("file.txt", "r") as f:\n    content = f.read()',
                'match_case': 'match value:\n    case 1:\n        print("One")\n    case 2 | 3:\n        print("Two or Three")\n    case _:\n        print("Other")'
            },
            'advanced_concepts': {
                'itertools': 'import itertools\nperms = list(itertools.permutations([1, 2, 3]))\ncombos = list(itertools.combinations([1, 2, 3, 4], 2))',
                'functools': 'from functools import reduce, partial\nsum_all = reduce(lambda x, y: x + y, [1, 2, 3, 4])\ndouble = partial(lambda x, y: x * y, 2)',
                'asyncio': 'import asyncio\n\nasync def fetch_data():\n    await asyncio.sleep(1)\n    return "data"\n\nasync def main():\n    result = await fetch_data()',
                'type_hints': 'from typing import List, Dict, Optional\n\ndef process_data(items: List[int]) -> Dict[str, int]:\n    return {"count": len(items)}',
                'dataclass': 'from dataclasses import dataclass\n\n@dataclass\nclass Person:\n    name: str\n    age: int\n    active: bool = True',
                'enum': 'from enum import Enum\n\nclass Status(Enum):\n    PENDING = 1\n    RUNNING = 2\n    COMPLETED = 3'
            },
            'django_examples': {
                'model': 'class User(models.Model):\n    name = models.CharField(max_length=100)\n    email = models.EmailField()\n    created_at = models.DateTimeField(auto_now_add=True)',
                'model_advanced': 'class Post(models.Model):\n    title = models.CharField(max_length=200)\n    author = models.ForeignKey(User, on_delete=models.CASCADE)\n    tags = models.ManyToManyField("Tag")\n    \n    class Meta:\n        ordering = ["-created_at"]\n        verbose_name_plural = "Posts"',
                'serializer': 'class UserSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = User\n        fields = ["id", "name", "email"]',
                'serializer_advanced': 'class PostSerializer(serializers.ModelSerializer):\n    author_name = serializers.CharField(source="author.name", read_only=True)\n    tag_names = serializers.SerializerMethodField()\n    \n    def get_tag_names(self, obj):\n        return [tag.name for tag in obj.tags.all()]',
                'view': '@api_view(["GET"])\ndef get_users(request):\n    users = User.objects.all()\n    serializer = UserSerializer(users, many=True)\n    return Response(serializer.data)',
                'viewset': 'class UserViewSet(viewsets.ModelViewSet):\n    queryset = User.objects.all()\n    serializer_class = UserSerializer\n    filter_backends = [DjangoFilterBackend]\n    filterset_fields = ["name", "email"]',
                'url_pattern': 'urlpatterns = [\n    path("users/", get_users, name="users"),\n    path("users/<int:pk>/", get_user, name="user_detail"),\n]',
                'middleware': 'class CustomMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n    \n    def __call__(self, request):\n        # Before view\n        response = self.get_response(request)\n        # After view\n        return response',
                'admin': 'class UserAdmin(admin.ModelAdmin):\n    list_display = ["name", "email", "created_at"]\n    list_filter = ["created_at"]\n    search_fields = ["name", "email"]\n\nadmin.site.register(User, UserAdmin)',
                'signals': 'from django.db.models.signals import post_save\nfrom django.dispatch import receiver\n\n@receiver(post_save, sender=User)\ndef user_post_save(sender, instance, created, **kwargs):\n    if created:\n        print(f"New user created: {instance.name}")'
            },
            'algorithms_examples': {
                'bubble_sort': 'def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr',
                'quick_sort': 'def quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)',
                'binary_search': 'def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1',
                'fibonacci': 'def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)',
                'fibonacci_memoized': 'from functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fibonacci_memo(n):\n    if n <= 1:\n        return n\n    return fibonacci_memo(n-1) + fibonacci_memo(n-2)',
                'dfs': 'def dfs(graph, start, visited=None):\n    if visited is None:\n        visited = set()\n    visited.add(start)\n    for neighbor in graph[start]:\n        if neighbor not in visited:\n            dfs(graph, neighbor, visited)\n    return visited',
                'bfs': 'from collections import deque\n\ndef bfs(graph, start):\n    visited = set()\n    queue = deque([start])\n    while queue:\n        vertex = queue.popleft()\n        if vertex not in visited:\n            visited.add(vertex)\n            queue.extend(graph[vertex] - visited)\n    return visited'
            }
        },
        'useful_tips': {
            'python_zen': 'import this  # Para ver o Zen do Python',
            'debugging': 'import pdb; pdb.set_trace()  # Para debugging',
            'performance': 'import timeit  # Para medir performance',
            'formatting': 'name = "World"\nmessage = f"Hello, {name}!"  # f-strings',
            'unpacking': 'a, b, *rest = [1, 2, 3, 4, 5]  # Unpacking',
            'walrus_operator': 'if (n := len(data)) > 10:\n    print(f"Large dataset: {n} items")',
            'context_managers': 'with open("file.txt") as f:\n    data = f.read()  # Automatically closes file',
            'comprehensions': 'squares = [x**2 for x in range(10) if x % 2 == 0]',
            'pathlib': 'from pathlib import Path\nfile_path = Path("data") / "file.txt"',
            'environment_vars': 'import os\ndb_url = os.getenv("DATABASE_URL", "default_value")',
            'logging': 'import logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)',
            'json_handling': 'import json\ndata = json.loads(json_string)\njson_string = json.dumps(data, indent=2)',
            'datetime': 'from datetime import datetime, timedelta\nnow = datetime.now()\ntomorrow = now + timedelta(days=1)',
            'regex': 'import re\npattern = r"\\d+"\nmatches = re.findall(pattern, "123 abc 456")',
            'virtual_env': 'python -m venv venv\nsource venv/bin/activate  # Linux/Mac\nvenv\\Scripts\\activate  # Windows',
            'pip_requirements': 'pip freeze > requirements.txt\npip install -r requirements.txt',
            'django_shell': 'python manage.py shell  # Django interactive shell',
            'django_migrations': 'python manage.py makemigrations\npython manage.py migrate',
            'django_superuser': 'python manage.py createsuperuser',
            'django_static': 'python manage.py collectstatic',
            'testing': 'python -m pytest  # Run tests with pytest\npython manage.py test  # Django tests',
            'list_methods': 'help(list)  # Ver métodos disponíveis',
            'object_attributes': 'dir(object)  # Ver atributos do objeto',
            'memory_usage': 'import sys\nsys.getsizeof(object)  # Tamanho em bytes',
            'pretty_print': 'import pprint\npprint.pprint(complex_data_structure)'
        },
        'best_practices': {
            'naming_conventions': {
                'variables': 'snake_case para variáveis e funções',
                'classes': 'PascalCase para classes',
                'constants': 'UPPER_CASE para constantes',
                'private': '_private_method para métodos privados'
            },
            'code_organization': {
                'imports': 'import padrão, import terceiros, import locais',
                'docstrings': 'def function():\n    """Descrição da função."""\n    pass',
                'error_handling': 'Seja específico com exceptions',
                'functions': 'Funções devem fazer uma coisa bem'
            },
            'django_best_practices': {
                'models': 'Use verbose_name e help_text',
                'views': 'Use class-based views quando apropriado',
                'urls': 'Use namespaces para apps',
                'settings': 'Separe settings por ambiente',
                'security': 'Use HTTPS, validação de entrada, CSRF protection'
            },
            'performance_tips': {
                'list_vs_generator': 'Use generators para economizar memória',
                'dict_lookup': 'Dicionários são O(1) para lookup',
                'string_joining': 'Use "".join(list) ao invés de += para strings',
                'comprehensions': 'List comprehensions são mais rápidas que loops',
                'caching': 'Use @lru_cache para memoização'
            }
        }
    })

@extend_schema(
    request=TwoSumSerializer,
    responses={
        200: {
            "type": "object",
            "properties": {
                "algorithm": {"type": "string", "example": "Two Sum"},
                "input": {
                    "type": "object",
                    "properties": {
                        "nums": {"type": "array", "items": {"type": "integer"}, "example": [2, 7, 11, 15]},
                        "target": {"type": "integer", "example": 9}
                    }
                },
                "result": {"type": "array", "items": {"type": "integer"}, "example": [0, 1]},
                "description": {"type": "string", "example": "Índices 0 e 1 somam 9"},
                "time_complexity": {"type": "string", "example": "O(n)"},
                "space_complexity": {"type": "string", "example": "O(n)"},
                "execution_time_ms": {"type": "number", "example": 1.23}
            }
        },
        400: {
            "type": "object", 
            "properties": {
                "error": {"type": "string", "example": "Dados de entrada inválidos"}
            }
        }
    },
    description="""
    **Two Sum Algorithm**
    
    Dado um array de inteiros `nums` e um inteiro `target`, retorna os índices dos dois números que somam o valor alvo.
    
    **Constraints:**
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9  
    - -10^9 <= target <= 10^9
    - Exatamente uma solução válida existe
    
    **Complexidade:**
    - Tempo: O(n) usando HashMap
    - Espaço: O(n) para armazenar os elementos visitados
    
    **Exemplos:**
    - Input: nums = [2,7,11,15], target = 9 → Output: [0,1]
    - Input: nums = [3,2,4], target = 6 → Output: [1,2]
    - Input: nums = [3,3], target = 6 → Output: [0,1]
    """,
    summary="Two Sum - Encontrar dois números que somam um valor alvo",
    tags=["Algorithms"]
)
@api_view(['POST'])
def two_sum(request):
    """Algoritmo Two Sum - Encontrar dois números que somam um valor alvo"""
    import time
    start_time = time.time()
    
    # Validar dados de entrada
    serializer = TwoSumSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({
            'error': 'Dados de entrada inválidos',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    nums = serializer.validated_data['nums']
    target = serializer.validated_data['target']
    
    try:
        # Implementação do Two Sum com HashMap - O(n)
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                execution_time = (time.time() - start_time) * 1000  # em ms
                result = [hashmap[complement], i]
                
                return Response({
                    'algorithm': 'Two Sum',
                    'input': {
                        'nums': nums,
                        'target': target
                    },
                    'result': result,
                    'description': f'Índices {result[0]} e {result[1]} somam {target}',
                    'explanation': f'nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}',
                    'time_complexity': 'O(n)',
                    'space_complexity': 'O(n)',
                    'execution_time_ms': round(execution_time, 3)
                })
            
            hashmap[num] = i
        
        # Se chegou aqui, não encontrou solução (não deveria acontecer segundo o problema)
        execution_time = (time.time() - start_time) * 1000
        return Response({
            'algorithm': 'Two Sum',
            'input': {
                'nums': nums,
                'target': target
            },
            'result': [],
            'description': 'Nenhuma solução encontrada',
            'time_complexity': 'O(n)',
            'space_complexity': 'O(n)',
            'execution_time_ms': round(execution_time, 3)
        })
        
    except Exception as e:
        return Response({
            'error': f'Erro interno: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
    request=AddTwoNumbersSerializer,
    responses={
        200: {
            "type": "object",
            "properties": {
                "algorithm": {"type": "string", "example": "Add Two Numbers"},
                "input": {
                    "type": "object",
                    "properties": {
                        "l1": {"type": "array", "items": {"type": "integer"}, "example": [2, 4, 3]},
                        "l2": {"type": "array", "items": {"type": "integer"}, "example": [5, 6, 4]}
                    }
                },
                "result": {"type": "array", "items": {"type": "integer"}, "example": [7, 0, 8]},
                "description": {"type": "string", "example": "342 + 465 = 807"},
                "time_complexity": {"type": "string", "example": "O(max(m,n))"},
                "space_complexity": {"type": "string", "example": "O(max(m,n))"},
                "execution_time_ms": {"type": "number", "example": 1.23}
            }
        },
        400: {
            "type": "object", 
            "properties": {
                "error": {"type": "string", "example": "Dados de entrada inválidos"}
            }
        }
    },
    description="""
    **Add Two Numbers Algorithm**
    
    Você recebe duas linked lists não vazias representando dois inteiros não negativos. 
    Os dígitos são armazenados em ordem reversa, e cada nó contém um único dígito.
    Some os dois números e retorne a soma como uma linked list.
    
    **Representação:**
    - [2,4,3] representa o número 342
    - [5,6,4] representa o número 465
    - Resultado [7,0,8] representa 807 (342 + 465)
    
    **Constraints:**
    - 1 <= número de nós <= 100
    - 0 <= valor do nó <= 9
    - Não há leading zeros (exceto para o número 0)
    
    **Complexidade:**
    - Tempo: O(max(m,n)) onde m e n são os comprimentos das listas
    - Espaço: O(max(m,n)) para armazenar o resultado
    
    **Exemplos:**
    - Input: l1=[2,4,3], l2=[5,6,4] → Output: [7,0,8] (342 + 465 = 807)
    - Input: l1=[0], l2=[0] → Output: [0]
    - Input: l1=[9,9,9,9,9,9,9], l2=[9,9,9,9] → Output: [8,9,9,9,0,0,0,1]
    """,
    summary="Add Two Numbers - Somar dois números representados como linked lists",
    tags=["Algorithms"]
)
@api_view(['POST'])
def add_two_numbers(request):
    """Algoritmo Add Two Numbers - Somar dois números em linked lists"""
    import time
    start_time = time.time()
    
    # Validar dados de entrada
    serializer = AddTwoNumbersSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({
            'error': 'Dados de entrada inválidos',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    l1 = serializer.validated_data['l1']
    l2 = serializer.validated_data['l2']
    
    try:
        # Implementação do Add Two Numbers
        result = []
        carry = 0
        i, j = 0, 0
        
        # Processar enquanto houver dígitos ou carry
        while i < len(l1) or j < len(l2) or carry:
            # Pegar o dígito atual de cada lista (0 se já terminou)
            digit1 = l1[i] if i < len(l1) else 0
            digit2 = l2[j] if j < len(l2) else 0
            
            # Calcular a soma
            total = digit1 + digit2 + carry
            
            # O dígito atual é o resto da divisão por 10
            result.append(total % 10)
            
            # O carry é o quociente da divisão por 10
            carry = total // 10
            
            # Avançar os índices
            i += 1
            j += 1
        
        execution_time = (time.time() - start_time) * 1000  # em ms
        
        # Converter arrays para números para mostrar na explicação
        num1 = sum(digit * (10 ** idx) for idx, digit in enumerate(l1))
        num2 = sum(digit * (10 ** idx) for idx, digit in enumerate(l2))
        result_num = sum(digit * (10 ** idx) for idx, digit in enumerate(result))
        
        return Response({
            'algorithm': 'Add Two Numbers',
            'input': {
                'l1': l1,
                'l2': l2
            },
            'result': result,
            'description': f'{num1} + {num2} = {result_num}',
            'explanation': f'Lista {l1} representa {num1}, lista {l2} representa {num2}, resultado {result} representa {result_num}',
            'time_complexity': 'O(max(m,n))',
            'space_complexity': 'O(max(m,n))',
            'execution_time_ms': round(execution_time, 3),
            'steps_details': {
                'l1_as_number': num1,
                'l2_as_number': num2,
                'result_as_number': result_num,
                'carry_operations': 'Processamento com carry bit a bit'
            }
        })
        
    except Exception as e:
        return Response({
            'error': f'Erro interno: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
