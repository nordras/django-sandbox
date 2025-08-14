from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import SandboxAPIViewSet

# Router para API REST
router = DefaultRouter()
router.register(r'api', SandboxAPIViewSet, basename='sandbox-api')

app_name = 'sandbox'

urlpatterns = [
    # Interface Web (Original)
    path('', views.algorithm_list, name='algorithm_list'),
    path('run/<int:algorithm_id>/', views.run_algorithm, name='run_algorithm'),
    
    # API REST com Swagger
    path('api/', include(router.urls)),
]
