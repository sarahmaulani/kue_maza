import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=admin,
            email=email,
            password=admin123
        )
        print("Superuser created")
    else:
        print("Superuser already exists")
else:
    print("Environment variables not set")
