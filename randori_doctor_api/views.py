from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Room, Leader, Participant, Session
from .serializers import (
    RoomSerializer, LeaderSerializer, ParticipantSerializer, SessionSerializer,
    TwoSumSerializer, TwoSumResponseSerializer
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
    description="""
    **Two Sum Algorithm**
    
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
    
    **Constraints:**
    - 2 ≤ nums.length ≤ 10⁴
    - -10⁹ ≤ nums[i] ≤ 10⁹  
    - -10⁹ ≤ target ≤ 10⁹
    - Only one valid answer exists
    
    **Algorithm Complexity:**
    - Time: O(n) - Single pass through the array
    - Space: O(n) - Hash map storage
    
    **Examples:**
    - Input: nums = [2,7,11,15], target = 9 → Output: [0,1]
    - Input: nums = [3,2,4], target = 6 → Output: [1,2]  
    - Input: nums = [3,3], target = 6 → Output: [0,1]
    """,
    summary="Two Sum - Find indices of two numbers that add up to target",
    request=TwoSumSerializer,
    responses={
        200: TwoSumResponseSerializer,
        400: {
            "type": "object",
            "properties": {
                "error": {"type": "string", "example": "Invalid input data"}
            }
        }
    },
    tags=["Algorithms"]
)
@api_view(['POST'])
def two_sum(request):
    """
    Two Sum Algorithm Implementation
    
    Uses hash map approach for O(n) time complexity.
    """
    serializer = TwoSumSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response({
            'error': 'Invalid input data',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    nums = serializer.validated_data['nums']
    target = serializer.validated_data['target']
    
    # Two Sum Algorithm - Hash Map Approach
    # Time: O(n), Space: O(n)
    hashmap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hashmap:
            # Found the solution
            indices = [hashmap[complement], i]
            values = [nums[indices[0]], nums[indices[1]]]
            
            response_data = {
                'indices': indices,
                'nums': nums,
                'target': target,
                'values': values,
                'explanation': f"nums[{indices[0]}] + nums[{indices[1]}] = {values[0]} + {values[1]} = {target}"
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        hashmap[num] = i
    
    # This should never happen according to problem constraints
    return Response({
        'error': 'No solution found',
        'message': 'According to problem constraints, a solution should always exist'
    }, status=status.HTTP_404_NOT_FOUND)
