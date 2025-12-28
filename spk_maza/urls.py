from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # ← TAMBAH INI

# Buat fungsi untuk halaman utama
def home_page(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kue Maza - Berhasil Deploy!</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            .success { color: green; font-size: 24px; margin-bottom: 20px; }
            .info { color: #666; margin-top: 30px; }
        </style>
    </head>
    <body>
        <div class="success">✅ Deployment Django BERHASIL!</div>
        <h1>Selamat datang di Kue Maza</h1>
        <p>Aplikasi Django kamu sudah online di Railway 🚀</p>
        <div class="info">
            <p><a href="/admin/">Admin Panel</a></p>
            <p><a href="/spk/">Aplikasi SPK</a></p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home_page, name='home'),  # ← INI YANG PENTING! Halaman utama
    path('admin/', admin.site.urls),
    path('spk/', include('spk.urls')), 
]
