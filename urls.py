from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

def redirect_to_api(request):
    return HttpResponseRedirect('/api/')

urlpatterns = [
    path('', redirect_to_api, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('randori_doctor_api.urls')),
    path('sandbox/', include('sandbox.urls')),
]
