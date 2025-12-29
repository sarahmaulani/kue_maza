import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spk_maza.settings')

application = get_wsgi_application()

# ⬇⬇⬇ BARU DI SINI ⬇⬇⬇
try:
    import spk.init_admin
    spk.init_admin.run()
except Exception as e:
    print("Init admin skipped:", e)
