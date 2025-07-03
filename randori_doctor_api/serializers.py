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
        help_text="Array of integers (2 to 10,000 elements)"
    )
    target = serializers.IntegerField(
        min_value=-1000000000,
        max_value=1000000000,
        help_text="Target sum value"
    )

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
