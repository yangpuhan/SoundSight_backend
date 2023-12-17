from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user_auth.models import UserHistory, UserProfile, User, AudioInfo

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
@require_http_methods(["GET"])
def user_info(request):
    user = request.user
    return JsonResponse({'code': 0, 'info': 'Succeed getting user info', 'data': {'username': user.username, 'id': user.id}})

# @login_required()
# @csrf_exempt
# @require_http_methods(["POST"])
# def prompt(request):
#     body = json.loads(request.body.decode("utf-8"))  
#     user_id = body.get('user_id')
#     text = body.get('text')
#     if user_id is None:
#         return JsonResponse({'code': 1, 'info': 'Invalid user_id'}, status=400)
#     user = User.objects.get(id=user_id)
#     if user is None:
#         return JsonResponse({'code': 4, 'info': 'Invalid user_id'}, status=400)
    
#     GPT_call.endpointmanager.add_endpoint_by_info(
#         api_key=GPT_call.OPENAI_API_KEY,
#         organization=GPT_call.OPENAI_API_ORGANIZATION
#     )
#     role_content_pair = {
#         "role": "user",
#         "content": text
#     }
    
#     response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, [role_content_pair], 512, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
#     content = GPT_call.GPT_related.get_content_from_response(response)
    
#     if user.history is None:
#         history_json = json.dumps([{"text": text, "response": content}])
#         user.history = UserHistory.objects.create(user_id=user_id, history_json=history_json)
#     else:
#         history_json = json.loads(user.history.history_json)
#         history_json.append({"text": text, "response": content})
#         user.history.history_json = json.dumps(history_json)
#         user.history.save()
    
#     user.save()
#     return JsonResponse({'code': 0, 'info': 'Succeed Prompt'})

@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def realtime_begin(request):
    body = json.loads(request.body.decode("utf-8"))  
    checkCode = body.get('checkCode')
    instruction = body.get('instruction')
    AudioInfo.objects.create(checkCode=checkCode, instruction=instruction)
    return JsonResponse({'code': 0, 'info': 'Succeed Linking', checkCode: checkCode})

@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def realtime_middle(request):
    body = json.loads(request.body.decode("utf-8"))  
    checkCode = body.get('checkCode')
    text = body.get('audioData')
    info = AudioInfo.objects.get(checkCode=checkCode)
    if info is None:
        return JsonResponse({'code': 1, 'info': 'Invalid checkCode'}, status=400)
    if info.text is None:
        info.text = text
    else:
        info.text = info.text + text  
    info.save() 
    return JsonResponse({'code': 0, 'info': 'Succeed receiving', "checkCode": checkCode})   

# @login_required()
@csrf_exempt
@require_http_methods(["POST"])
def realtime_end(request):
    # body = json.loads(request.body.decode("utf-8"))  
    # checkCode = body.get('checkCode')
    # text = body.get('audioData')
    # info = AudioInfo.objects.get(checkCode=checkCode)
    # if info is None:
    #     return JsonResponse({'code': 1, 'info': 'Invalid checkCode'}, status=400)
    # if info.text is None:
    #     info.text = text
    # else:
    #     info.text = info.text + text
    # origin = info.text
    # info.save()
    
    GPT_call.endpointmanager.add_endpoint_by_info(
        api_key=GPT_call.OPENAI_API_KEY,
        organization=GPT_call.OPENAI_API_ORGANIZATION
    )
    content = {
        "instruction": "我现在在学习，帮我总结出几个相关的topic",
        "user.name": "王煜焜",
        "user.age": 20,
        "user.job": "University Student",
        "user.hobby": ["Basketball"],
        "user.school": "Tsinghua University",
        "user.major": ["Computer Science and Technology", "Finance"],
        "user.rules": [
            "Pay attention to the discussion about classes",
            "Pay less attention to other people's intimate topics"
        ],
        "context.date_time": "2023-07-25 20:43:11",
        "context.day_of_week": "Tuesday",
        "context.wifi_name": "\"Tsinghua-Secure\"",
        "context.bluetooth_devices": "HUAWEI WATCH GT 2-92A",
        "context.location": "北京市海淀区日新路6号靠近清华大学FIT楼",
        "context.activity": "still",
        "sound": [
            {
                "speaker": "Unknown-01",
                "content": "牛肉面好吃捏",
            },
            {
                "speaker": "Unknown-02",
                "content": "麦当劳好贵啊",
            },
            {
                "speaker": "Unknown-03",
                "content": "计组的中断异常很难搞啊",
            },
            {
                "speaker": "Unknown-04",
                "content": "我觉得这个老师讲计组将的很好啊",
            },
            {
                "speaker": "Unknown-05",
                "content": "我们应该能写到ucore吧？",
            }
        ],
    }
    role_content_pair = {
        "role": "user",
        "content": json.dumps(content,ensure_ascii=False)
    }
    response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.instruction_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
    content = GPT_call.GPT_related.get_content_from_response(response)
    content = json.loads(content)
    
    # return JsonResponse({'code': 0, 'info': 'Succeed receiving', "checkCode": checkCode, 'content': content, 'origin': origin})
    return JsonResponse({'code': 0, 'info': 'Succeed receiving', 'content': content})
    

