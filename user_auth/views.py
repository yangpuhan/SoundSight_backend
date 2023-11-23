from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user_auth.models import UserHistory, UserProfile, User

import json
from . import GPT_call

@csrf_exempt
def index(request):
    return JsonResponse({'code': 0, 'info': 'Succeed Startup'})


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    body = json.loads(request.body.decode("utf-8"))
    identity = body.get('username')
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

@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def prompt(request):
    body = json.loads(request.body.decode("utf-8"))  
    user_id = body.get('user_id')
    text = body.get('text')
    if user_id is None:
        return JsonResponse({'code': 1, 'info': 'Invalid user_id'}, status=400)
    user = User.objects.get(id=user_id)
    if user is None:
        return JsonResponse({'code': 4, 'info': 'Invalid user_id'}, status=400)
    
    GPT_call.endpointmanager.add_endpoint_by_info(
        api_key=GPT_call.OPENAI_API_KEY,
        organization=GPT_call.OPENAI_API_ORGANIZATION
    )
    role_content_pair = {
        "role": "user",
        "content": text
    }
    
    response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, [role_content_pair], 512, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
    content = GPT_call.GPT_related.get_content_from_response(response)
    
    if user.history is None:
        history_json = json.dumps([{"text": text, "response": content}])
        user.history = UserHistory.objects.create(user_id=user_id, history_json=history_json)
    else:
        history_json = json.loads(user.history.history_json)
        history_json.append({"text": text, "response": content})
        user.history.history_json = json.dumps(history_json)
        user.history.save()
    
    user.save()
    return JsonResponse({'code': 0, 'info': 'Succeed Prompt'})

