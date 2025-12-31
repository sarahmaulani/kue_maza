# spk/migrations/0003_add_tahun_to_periode.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('spk', '0002_add_alamat'),
    ]
    
    operations = [
        migrations.AddField(
            model_name='periode',
            name='tahun',
            field=models.IntegerField(default=2024),
        ),
    ]
