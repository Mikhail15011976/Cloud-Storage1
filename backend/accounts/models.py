from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    storage_limit = models.BigIntegerField(default=5368709120)  # 5GB по умолчанию
    
    def __str__(self):
        return self.username