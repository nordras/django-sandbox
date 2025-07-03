from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

def redirect_to_api(request):
    return HttpResponseRedirect('/api/')

urlpatterns = [
    path('', redirect_to_api, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('randori_doctor_api.urls')),
    # URLs do Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
