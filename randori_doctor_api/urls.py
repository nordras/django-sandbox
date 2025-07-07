from rest_framework.routers import DefaultRouter
from .views import (
    RoomViewSet, LeaderViewSet, ParticipantViewSet, SessionViewSet, 
    hello_world, two_sum, add_two_numbers
)
from django.urls import path, include

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', hello_world, name='hello_world'),
    path('two-sum/', two_sum, name='two_sum'),
    path('add-two-numbers/', add_two_numbers, name='add_two_numbers'),
]
