from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from django.shortcuts import render
from django.http import JsonResponse
import time
import json

from .serializers import (
    AlgorithmSerializer, 
    AlgorithmResultSerializer, 
    BatchExecutionResultSerializer,
    TwoSumInputSerializer,
    BinarySearchInputSerializer,
    StringInputSerializer,
    AnagramInputSerializer,
    MergeArraysInputSerializer
)

# Importar algoritmos originais
from .views import ALGORITHMS, execute_algorithm as original_execute_algorithm


class SandboxAPIViewSet(ViewSet):
    """
    ViewSet completo para Sandbox de Algoritmos
    
    Fornece endpoints para listar, executar e testar algoritmos de programação
    com entrada personalizada e métricas de performance.
    """

    @extend_schema(
        summary="Listar todos os algoritmos disponíveis",
        description="Retorna lista completa de algoritmos implementados no sandbox",
        responses={200: AlgorithmSerializer(many=True)},
        tags=["Sandbox"]
    )
    def list(self, request):
        """Lista todos os algoritmos disponíveis"""
        serializer = AlgorithmSerializer(ALGORITHMS, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Executar algoritmo específico",
        description="Executa um algoritmo pelo ID com dados pré-definidos",
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='ID do algoritmo (1-9)'
            )
        ],
        responses={
            200: AlgorithmResultSerializer,
            404: OpenApiTypes.OBJECT
        },
        examples=[
            OpenApiExample(
                'Exemplo Two Sum',
                summary='Execução do algoritmo Two Sum',
                description='Resultado da execução do Two Sum com dados padrão',
                value={
                    "algorithm": "Two Sum",
                    "result": [0, 1],
                    "execution_time_ms": 0.05,
                    "input_data": {"nums": [2, 7, 11, 15], "target": 9}
                }
            )
        ],
        tags=["Sandbox"]
    )
    def retrieve(self, request, pk=None):
        """Executa um algoritmo específico pelo ID"""
        try:
            algorithm_id = int(pk)
            algorithm = next((alg for alg in ALGORITHMS if alg['id'] == algorithm_id), None)
            
            if not algorithm:
                return Response(
                    {'error': f'Algoritmo com ID {algorithm_id} não encontrado'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Medir tempo de execução
            start_time = time.time()
            result = original_execute_algorithm(algorithm['function'])
            execution_time = (time.time() - start_time) * 1000
            
            # Obter dados de entrada padrão
            input_data = self._get_default_input(algorithm['function'])
            
            response_data = {
                'algorithm': algorithm['name'],
                'result': result,
                'execution_time_ms': round(execution_time, 3),
                'input_data': input_data
            }
            
            serializer = AlgorithmResultSerializer(response_data)
            return Response(serializer.data)
            
        except ValueError:
            return Response(
                {'error': 'ID do algoritmo deve ser um número inteiro'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': f'Erro na execução: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        summary="Executar todos os algoritmos",
        description="Executa todos os algoritmos disponíveis e retorna resultados com métricas",
        responses={200: BatchExecutionResultSerializer},
        examples=[
            OpenApiExample(
                'Execução em lote',
                summary='Resultado da execução de todos os algoritmos',
                value={
                    "total_algorithms": 9,
                    "successful_executions": 9,
                    "failed_executions": 0,
                    "execution_time_ms": 15.234,
                    "results": {
                        "Two Sum": [0, 1],
                        "Reverse String": "olleh",
                        "Fibonacci": 55
                    }
                }
            )
        ],
        tags=["Sandbox"]
    )
    @action(detail=False, methods=['post'])
    def run_all(self, request):
        """Executa todos os algoritmos e retorna métricas"""
        start_time = time.time()
        results = {}
        successful = 0
        failed = 0
        
        for algorithm in ALGORITHMS:
            try:
                result = original_execute_algorithm(algorithm['function'])
                results[algorithm['name']] = result
                successful += 1
            except Exception as e:
                results[algorithm['name']] = f"Erro: {str(e)}"
                failed += 1
        
        total_time = (time.time() - start_time) * 1000
        
        response_data = {
            'total_algorithms': len(ALGORITHMS),
            'successful_executions': successful,
            'failed_executions': failed,
            'execution_time_ms': round(total_time, 3),
            'results': results
        }
        
        serializer = BatchExecutionResultSerializer(response_data)
        return Response(serializer.data)

    @extend_schema(
        summary="Executar Two Sum com entrada customizada",
        description="Executa algoritmo Two Sum com array e target personalizados",
        request=TwoSumInputSerializer,
        responses={200: AlgorithmResultSerializer},
        examples=[
            OpenApiExample(
                'Two Sum Customizado',
                summary='Entrada personalizada para Two Sum',
                description='Execute Two Sum com seus próprios dados',
                value={"nums": [3, 2, 4], "target": 6},
                request_only=True
            )
        ],
        tags=["Algoritmos Customizados"]
    )
    @action(detail=False, methods=['post'])
    def two_sum_custom(self, request):
        """Executa Two Sum com entrada personalizada"""
        serializer = TwoSumInputSerializer(data=request.data)
        if serializer.is_valid():
            from .views import two_sum
            
            nums = serializer.validated_data['nums']
            target = serializer.validated_data['target']
            
            start_time = time.time()
            result = two_sum(nums, target)
            execution_time = (time.time() - start_time) * 1000
            
            response_data = {
                'algorithm': 'Two Sum (Custom)',
                'result': result,
                'execution_time_ms': round(execution_time, 3),
                'input_data': serializer.validated_data
            }
            
            return Response(AlgorithmResultSerializer(response_data).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _get_default_input(self, function_name):
        """Retorna dados de entrada padrão para cada algoritmo"""
        defaults = {
            'two_sum': {"nums": [2, 7, 11, 15], "target": 9},
            'reverse_string': {"text": "hello"},
            'fibonacci': {"n": 10},
            'binary_search': {"arr": [1, 2, 3, 4, 5, 6, 7, 8, 9], "target": 5},
            'valid_palindrome': {"text": "A man, a plan, a canal: Panama"},
            'remove_duplicates': {"nums": [1, 1, 2, 2, 3, 4, 4, 5]},
            'merge_sorted_arrays': {"array1": [1, 3, 5], "array2": [2, 4, 6]},
            'contains_duplicate': {"nums": [1, 2, 3, 1]},
            'valid_anagram': {"string1": "listen", "string2": "silent"}
        }
        return defaults.get(function_name, {})


# Manter view original para interface web
def algorithm_list(request):
    """Página com lista de algoritmos para testar"""
    return render(request, 'sandbox/algorithm_list.html', {'algorithms': ALGORITHMS})


def run_algorithm(request, algorithm_id):
    """Executar um algoritmo específico"""
    algorithm = next((alg for alg in ALGORITHMS if alg['id'] == algorithm_id), None)
    
    if not algorithm:
        return JsonResponse({'error': 'Algoritmo não encontrado'}, status=404)
    
    result = original_execute_algorithm(algorithm['function'])
    
    return JsonResponse({
        'algorithm': algorithm['name'],
        'result': result
    })
