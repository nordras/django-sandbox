from rest_framework import serializers
from .models import Room, Leader, Participant, Session

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class TwoSumSerializer(serializers.Serializer):
    nums = serializers.ListField(
        child=serializers.IntegerField(),
        min_length=2,
        max_length=10000,
        help_text="Array de inteiros (2 <= length <= 10000)"
    )
    target = serializers.IntegerField(
        min_value=-1000000000,
        max_value=1000000000,
        help_text="Valor alvo (-10^9 <= target <= 10^9)"
    )

    def validate_nums(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Array deve ter pelo menos 2 elementos")
        if len(value) > 10000:
            raise serializers.ValidationError("Array não pode ter mais de 10000 elementos")
        return value

class TwoSumResponseSerializer(serializers.Serializer):
    indices = serializers.ListField(
        child=serializers.IntegerField(),
        help_text="Indices of the two numbers that add up to target"
    )
    nums = serializers.ListField(
        child=serializers.IntegerField(),
        help_text="Original input array"
    )
    target = serializers.IntegerField(help_text="Target sum")
    values = serializers.ListField(
        child=serializers.IntegerField(),
        help_text="The actual values at the found indices"
    )
    explanation = serializers.CharField(help_text="Explanation of the solution")
