from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    body = json.loads(request.body.decode("utf-8"))
    identity = body.get('username')
    password = body.get('password')

    if len(identity) > 50 or len(password) != 64:
        return JsonResponse({'code': 2, 'info': 'Invalid username or password format'}, status=400)

    if User.objects.filter(username=identity).exists():
        return JsonResponse({'code': 1, 'info': 'Username already exists'}, status=400)

    User.objects.create_user(username=identity, password=password)
    return JsonResponse({'code': 0, 'info': 'Succeed Register'})

@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    body = json.loads(request.body.decode("utf-8"))
    identity = body.get('username')
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

