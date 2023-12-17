from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user_auth.models import UserHistory, UserProfile, User, AudioInfo
from gpt_related import GPT_call
import json

@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def polish(request):
    body = json.loads(request.body.decode("utf-8"))  
    text = body.get('text')

    
    GPT_call.endpointmanager.add_endpoint_by_info(
        api_key=GPT_call.OPENAI_API_KEY,
        organization=GPT_call.OPENAI_API_ORGANIZATION
    )
    role_content_pair = {
        "role": "user",
        "content": text
    }
    
    response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.polish_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
    content = GPT_call.GPT_related.get_content_from_response(response)

    return JsonResponse({'code': 0, 'info': 'Succeed polishing', "polished_text": content})
    

