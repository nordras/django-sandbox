from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Room, Leader, Participant, Session
from .serializers import (
    RoomSerializer, LeaderSerializer, ParticipantSerializer, SessionSerializer,
    TwoSumSerializer, TwoSumResponseSerializer, AddTwoNumbersSerializer,
    PythonSyntaxSerializer
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
    description="Endpoint Hello World simples para testar a API",
    summary="Hello World",
    responses={
        200: {
            "type": "object",
            "properties": {
                "message": {"type": "string", "example": "Hello World!"},
                "status": {"type": "string", "example": "success"},
                "data": {
                    "type": "object",
                    "properties": {
                        "framework": {"type": "string", "example": "Django REST Framework"},
                        "version": {"type": "string", "example": "1.0.0"},
                        "description": {"type": "string", "example": "Meu primeiro endpoint Django!"}
                    }
                }
            }
        }
    },
    tags=["Hello World"]
)
@api_view(['GET'])
def hello_world(request):
    """Endpoint Hello World simples"""
    return Response({
        'message': 'Hello World!',
        'status': 'success',
        'data': {
            'framework': 'Django REST Framework',
            'version': '1.0.0',
            'description': 'Meu primeiro endpoint Django!'
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
