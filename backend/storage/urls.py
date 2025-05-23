from django.urls import path
from .views import FileListView, FileDetailView

urlpatterns = [
    path('', FileListView.as_view(), name='file-list'),
    path('<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('user/<int:user_id>/', FileListView.as_view(), name='user-file-list'),
]