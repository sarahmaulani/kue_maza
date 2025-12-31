from django.urls import path
from .views import (
    user_home, 
    user_login, 
    user_logout,  
    hasil_topsis, 
    index, 
    input_nilai, 
    analytics_dashboard, 
    export_report
)

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.user_home, name='user_home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('hasil/', views.hasil_topsis, name='hasil_topsis'),
    path('hasil/<int:periode_id>/', views.hasil_topsis, name='hasil_topsis_periode'),
    path('input-nilai/', views.input_nilai, name='input_nilai'),  # ← INI
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),  # ← INI
    path('export/<str:report_type>/', views.export_report, name='export_report'),
]
