import os
import sys

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spk_maza.settings')

application = get_wsgi_application()

# ⬇⬇⬇ BARU DI SINI ⬇⬇⬇
try:
    import spk.init_admin
    spk.init_admin.run()
except Exception as e:
    print("Init admin skipped:", e)
