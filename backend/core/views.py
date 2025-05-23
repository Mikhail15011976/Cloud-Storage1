from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

def home(request):
    # Для API запросов
    if request.headers.get('Accept') == 'application/json':
        response_data = {
            'message': 'Welcome to Cloud Storage API',
            'endpoints': {
                'admin': '/admin/',
                'api_docs': '/api/docs/',
                'register': '/api/auth/register/',
                'login': '/api/auth/token/',
                'files': '/api/files/',
                'users': '/api/users/'
            }
        }
        
        # Добавляем информацию о пользователе, если он авторизован
        if request.user.is_authenticated:
            token, _ = Token.objects.get_or_create(user=request.user)
            response_data['user'] = {
                'username': request.user.username,
                'is_admin': request.user.is_admin,
                'token': token.key
            }
            
        return JsonResponse(response_data)
    
    # Для браузерных запросов
    context = {
        'user_authenticated': request.user.is_authenticated,
        'is_admin': request.user.is_authenticated and request.user.is_admin
    }
    return render(request, 'index.html', context)