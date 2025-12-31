# migrate.py
import os
import django
import sys

sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spk_maza.settings')
django.setup()

from django.core.management import execute_from_command_line

# Jalankan migrasi
execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
print("Database migrated successfully")

# Buat superuser
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser 'admin' created with password 'admin123'")
