from django.shortcuts import render
from django.http import JsonResponse

# Lista simples de algoritmos para testar
ALGORITHMS = [
    {
        'id': 1,
        'name': 'Two Sum',
        'description': 'Encontrar dois números em um array que somam um target',
        'function': 'two_sum'
    },
    {
        'id': 2,
        'name': 'Reverse String',
        'description': 'Inverter uma string',
        'function': 'reverse_string'
    },
    {
        'id': 3,
        'name': 'Fibonacci',
        'description': 'Calcular sequência de Fibonacci',
        'function': 'fibonacci'
    },
    {
        'id': 4,
        'name': 'Binary Search',
        'description': 'Busca binária em array ordenado',
        'function': 'binary_search'
    }
]

def algorithm_list(request):
    """Página com lista de algoritmos para testar"""
    return render(request, 'sandbox/algorithm_list.html', {'algorithms': ALGORITHMS})

def run_algorithm(request, algorithm_id):
    """Executar um algoritmo específico"""
    algorithm = next((alg for alg in ALGORITHMS if alg['id'] == algorithm_id), None)
    
    if not algorithm:
        return JsonResponse({'error': 'Algoritmo não encontrado'}, status=404)
    
    # Aqui você pode executar o algoritmo e retornar os resultados
    result = execute_algorithm(algorithm['function'])
    
    return JsonResponse({
        'algorithm': algorithm['name'],
        'result': result
    })

def execute_algorithm(function_name):
    """Executar algoritmos baseados no nome da função"""
    if function_name == 'two_sum':
        return two_sum([2, 7, 11, 15], 9)
    elif function_name == 'reverse_string':
        return reverse_string("hello")
    elif function_name == 'fibonacci':
        return fibonacci(10)
    elif function_name == 'binary_search':
        return binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    else:
        return "Algoritmo não implementado"

# Implementações dos algoritmos
def two_sum(nums, target):
    """Algoritmo Two Sum"""
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

def reverse_string(s):
    """Inverter string"""
    return s[::-1]

def fibonacci(n):
    """Sequência de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def binary_search(arr, target):
    """Busca binária"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
