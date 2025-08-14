from rest_framework import serializers


class AlgorithmSerializer(serializers.Serializer):
    """Serializer para informações do algoritmo"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    function = serializers.CharField(max_length=50)


class AlgorithmResultSerializer(serializers.Serializer):
    """Serializer para resultado da execução do algoritmo"""
    algorithm = serializers.CharField(max_length=100)
    result = serializers.JSONField()
    execution_time_ms = serializers.FloatField(required=False)
    input_data = serializers.JSONField(required=False)


class BatchExecutionResultSerializer(serializers.Serializer):
    """Serializer para execução em lote de algoritmos"""
    total_algorithms = serializers.IntegerField()
    successful_executions = serializers.IntegerField()
    failed_executions = serializers.IntegerField()
    execution_time_ms = serializers.FloatField()
    results = serializers.DictField(child=serializers.JSONField())


class AlgorithmInputSerializer(serializers.Serializer):
    """Serializer para entrada customizada de algoritmos"""
    algorithm_id = serializers.IntegerField()
    input_data = serializers.JSONField()


class TwoSumInputSerializer(serializers.Serializer):
    """Serializer específico para Two Sum"""
    nums = serializers.ListField(child=serializers.IntegerField())
    target = serializers.IntegerField()


class BinarySearchInputSerializer(serializers.Serializer):
    """Serializer específico para Binary Search"""
    arr = serializers.ListField(child=serializers.IntegerField())
    target = serializers.IntegerField()


class StringInputSerializer(serializers.Serializer):
    """Serializer para algoritmos que recebem string"""
    text = serializers.CharField(max_length=1000)


class AnagramInputSerializer(serializers.Serializer):
    """Serializer para Valid Anagram"""
    string1 = serializers.CharField(max_length=1000)
    string2 = serializers.CharField(max_length=1000)


class MergeArraysInputSerializer(serializers.Serializer):
    """Serializer para Merge Sorted Arrays"""
    array1 = serializers.ListField(child=serializers.IntegerField())
    array2 = serializers.ListField(child=serializers.IntegerField())
