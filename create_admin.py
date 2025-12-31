# create_admin.py
import os
import django
import sys

sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spk_maza.settings')
django.setup()

from django.contrib.auth.models import User

# Hapus user admin lama jika ada
User.objects.filter(username='admin').delete()

# Buat user admin baru
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)
print(f"Superuser 'admin' created with password 'admin123'")

# Buat UserProfile untuk admin
from spk.models import UserProfile
UserProfile.objects.create(
    user=user,
    role='admin',
    phone='08123456789',
    department='Management'
)
print("UserProfile created for admin")
