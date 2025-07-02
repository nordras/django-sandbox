from django.urls import path
from . import views

app_name = 'sandbox'

urlpatterns = [
    path('', views.algorithm_list, name='algorithm_list'),
    path('run/<int:algorithm_id>/', views.run_algorithm, name='run_algorithm'),
]
