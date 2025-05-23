import os
import uuid
from django.db import models
from django.conf import settings
from accounts.models import User

def user_directory_path(instance, filename):
    # Файлы будут загружены в MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    original_name = models.CharField(max_length=255)
    size = models.BigIntegerField()
    comment = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_download = models.DateTimeField(null=True, blank=True)
    download_count = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.original_name:
            self.original_name = os.path.basename(self.file.name)
        if not self.size and self.file:
            self.size = self.file.size
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.original_name} ({self.user.username})"