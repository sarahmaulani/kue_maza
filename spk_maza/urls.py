from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok", "service": "kue_maza"})

urlpatterns = [
    path('', health_check),  # Halaman utama jadi health check
    path('health/', health_check),  # Backup route
    # path('admin/', admin.site.urls),
    path('spk/', include('spk.urls')),
]
