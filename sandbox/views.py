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
    },
    {
        'id': 5,
        'name': 'Valid Palindrome',
        'description': 'Verificar se uma string é palíndromo',
        'function': 'valid_palindrome'
    },
    {
        'id': 6,
        'name': 'Remove Duplicates',
        'description': 'Remover duplicatas de array ordenado',
        'function': 'remove_duplicates'
    },
    {
        'id': 7,
        'name': 'Merge Sorted Arrays',
        'description': 'Combinar dois arrays ordenados',
        'function': 'merge_sorted_arrays'
    },
    {
        'id': 8,
        'name': 'Contains Duplicate',
        'description': 'Verificar se há duplicatas no array',
        'function': 'contains_duplicate'
    },
    {
        'id': 9,
        'name': 'Valid Anagram',
        'description': 'Verificar se duas strings são anagramas',
        'function': 'valid_anagram'
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
    elif function_name == 'valid_palindrome':
        return valid_palindrome("A man, a plan, a canal: Panama")
    elif function_name == 'remove_duplicates':
        return remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5])
    elif function_name == 'merge_sorted_arrays':
        return merge_sorted_arrays([1, 3, 5], [2, 4, 6])
    elif function_name == 'contains_duplicate':
        return contains_duplicate([1, 2, 3, 1])
    elif function_name == 'valid_anagram':
        return valid_anagram("listen", "silent")
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

def valid_palindrome(s):
    """Verificar se uma string é palíndromo"""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def remove_duplicates(nums):
    """Remover duplicatas de array ordenado"""
    if not nums:
        return []
    
    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            result.append(nums[i])
    return result

def merge_sorted_arrays(nums1, nums2):
    """Combinar dois arrays ordenados"""
    result = []
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result

def contains_duplicate(nums):
    """Verificar se há duplicatas no array"""
    return len(nums) != len(set(nums))

def valid_anagram(s, t):
    """Verificar se duas strings são anagramas"""
    return sorted(s.lower()) == sorted(t.lower())
