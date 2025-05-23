from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'original_name', 'size', 'comment', 'upload_date', 'last_download', 'download_count']
        read_only_fields = ['id', 'size', 'upload_date', 'last_download', 'download_count']