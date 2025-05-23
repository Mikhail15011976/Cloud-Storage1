import os
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from django.core.exceptions import PermissionDenied
from .models import File
from .serializers import FileSerializer
from accounts.models import User

class FileListView(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            if not self.request.user.is_admin:
                raise PermissionDenied("You don't have permission to access this resource.")
            return File.objects.filter(user_id=user_id)
        return File.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        file_obj = self.request.FILES['file']
        serializer.save(
            user=self.request.user,
            original_name=file_obj.name,
            size=file_obj.size
        )

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.last_download = timezone.now()
        instance.download_count += 1
        instance.save()
        
        file_path = instance.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{instance.original_name}"'
        return response