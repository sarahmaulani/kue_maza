# whitenoise_fix.py
import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='staticfiles')
