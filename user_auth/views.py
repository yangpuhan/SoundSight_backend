from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user_auth.models import UserHistory, UserProfile, User

@csrf_exempt
def index(request):
    return JsonResponse({'code': 0, 'info': 'Succeed Startup'})


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    body = json.loads(request.body.decode("utf-8"))
    identity = body.get('identity')
    password = body.get('password')
    
    if identity is None or password is None:
        return JsonResponse({'code': 3, 'info': 'Invalid username or password format'}, status=400)

    if len(identity) > 50:
        return JsonResponse({'code': 2, 'info': 'Invalid username or password format'}, status=400)

    if User.objects.filter(username=identity).exists():
        return JsonResponse({'code': 1, 'info': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=identity, password=password)
    return JsonResponse({'code': 0, 'info': 'Succeed Register','user': user.serialize()})

@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    body = json.loads(request.body.decode("utf-8"))
    identity = body.get('identity')
    password = body.get('password')

    user = authenticate(username=identity, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'code': 0, 'info': 'Succeed Login'})
    else:
        return JsonResponse({'code': 2, 'info': 'Invalid username or password'}, status=400)


@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({'code': 0, 'info': 'Succeed Logout'})

