#!/usr/bin/env python
"""
Auto create/reset admin user for Railway deployment
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spk_maza.settings')
django.setup()

from django.contrib.auth.models import User
from django.db.utils import OperationalError

def create_or_reset_admin():
    """Create or reset admin user with known password"""
    
    # Password yang SIMPLE untuk testing
    # Nanti bisa diganti setelah berhasil login
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = 'admin123'  # ← PASSWORD SIMPLE INI
    ADMIN_EMAIL = 'admin@example.com'
    
    try:
        # Cek koneksi database
        User.objects.count()
        
        # Cek apakah admin sudah ada
        if User.objects.filter(username=ADMIN_USERNAME).exists():
            user = User.objects.get(username=ADMIN_USERNAME)
            user.set_password(ADMIN_PASSWORD)
            user.is_staff = True
            user.is_superuser = True
            user.email = ADMIN_EMAIL
            user.save()
            print(f"✅ Admin user UPDATED: {ADMIN_USERNAME} / {ADMIN_PASSWORD}")
        else:
            # Buat admin baru
            User.objects.create_superuser(
                username=ADMIN_USERNAME,
                email=ADMIN_EMAIL,
                password=ADMIN_PASSWORD
            )
            print(f"✅ Admin user CREATED: {ADMIN_USERNAME} / {ADMIN_PASSWORD}")
        
        return True
        
    except OperationalError as e:
        print(f"❌ Database error: {e}")
        print("⚠️  Run migrations first: python manage.py migrate")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("Admin User Setup for Railway")
    print("=" * 50)
    
    success = create_or_reset_admin()
    
    if success:
        print("\n✅ Setup completed successfully!")
        print(f"\n📋 LOGIN INFO:")
        print(f"   URL: https://kuemaza-production.up.railway.app/admin/")
        print(f"   Username: admin")
        print(f"   Password: admin123")
        print("\n⚠️  Change password after first login!")
    else:
        print("\n❌ Setup failed!")
    
    sys.exit(0 if success else 1)
