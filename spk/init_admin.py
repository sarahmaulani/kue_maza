import os
from django.contrib.auth import get_user_model

def run():
    User = get_user_model()

    username = os.getenv("ADMIN_USERNAME", "admin")
    email = os.getenv("ADMIN_EMAIL", "admin@gmail.com")
    password = os.getenv("ADMIN_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
