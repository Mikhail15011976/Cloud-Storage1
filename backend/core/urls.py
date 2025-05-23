from django.contrib import admin
from accounts.views import RegisterView
from django.urls import path, include
from rest_framework.authtoken import views
from .views import home  # Импортируем наше новое представление
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Cloud Storage API",
      default_version='v1',
      description="API documentation for Cloud Storage",
   ),
   public=True,
)

urlpatterns = [
    path('', home, name='home'),  # Добавляем корневой URL
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', views.obtain_auth_token),
    path('api/users/', include('accounts.urls')),
    path('api/files/', include('storage.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]