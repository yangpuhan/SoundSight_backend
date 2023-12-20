from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from gpt_related.models import AudioInfo, FullAudio
from gpt_related import GPT_call
import json
import datetime

@login_required()
@csrf_exempt
@require_http_methods(["POST"])
def realtime_summary(request):
    body = json.loads(request.body.decode("utf-8"))  
    text = body.get('sound_new')
    instruction = body.get('instruction')
    checkCode = body.get('checkCode')

    role_content_pair = {
        "role": "user",
        "content": text
    }
    
    response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.polish_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
    polished = GPT_call.GPT_related.get_content_from_response(response)
    print("POLISH DONE")

    last_audio_info = AudioInfo.objects.filter(user=request.user, checkCode=checkCode).order_by('-created_time').first()
    if last_audio_info:
        last_output = json.loads(last_audio_info.json_text).get('last_output')
    else:
        last_output = ""
        
    role_content_pair = {
        "role": "user",
        "content": json.dumps({
            "last_output": last_output,
            "sound_new": polished,
            "instruction": instruction
        },ensure_ascii=False)
    }
    print(role_content_pair)

    response = GPT_call.GPT_related.connect_openai_api_chat(GPT_call.MODEL, GPT_call.realtime_prompt+[role_content_pair], 4000, GPT_call.logger, 30, ["debug", "[EXAMPLE]"])
    content = GPT_call.GPT_related.get_content_from_response(response)
    output = json.loads(content).get('topic')

    save_audio_info = AudioInfo(
        checkCode=checkCode,
        json_text=json.dumps({
            "last_output": output
        },ensure_ascii=False),
        user=request.user
    )
    save_audio_info.save()

    current_audio = FullAudio.objects.filter(user=request.user, checkCode=checkCode).first()
    if current_audio:
        cur_summary = current_audio.summary + output
        cur_text = current_audio.full_text + polished
        current_audio.summary = cur_summary
        current_audio.full_text = cur_text
        current_audio.updated_time = datetime.datetime.now().timestamp()
        current_audio.save()
    else:
        save_audio_summary = FullAudio(
            checkCode=checkCode,
            full_text=polished,
            summary=output,
            user=request.user
        )
        save_audio_summary.save()
    print(current_audio)

    return JsonResponse({'code': 0, 'info': 'Succeed response', "topics": output})
    

