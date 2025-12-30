# spk/migrations/0002_add_alamat.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('spk', '0001_initial'),
    ]
    
    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='alamat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
