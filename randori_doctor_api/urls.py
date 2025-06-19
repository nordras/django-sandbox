from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, LeaderViewSet, ParticipantViewSet, SessionViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
